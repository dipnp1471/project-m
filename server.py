#!/usr/bin/env python3
"""
MedBank Studio — Local Server & Direct Instagram Reels Publisher

Zero external Python dependencies (uses Python 3 standard library only).
Serves the MedBank Studio web app AND provides local REST endpoints to:
  1. Transcode browser recordings (.webm / .mp4) via FFmpeg into strict
     Instagram Reels-compatible H.264 + AAC MP4 (1080x1920, 30fps, faststart).
  2. Upload & publish Reels directly to Instagram via Meta's Instagram Graph API
     Resumable Upload flow (no Canva, no cloud storage bucket required).

Usage:
    python server.py
    python server.py --port 8080
"""

from __future__ import annotations

import argparse
import base64
import json
import mimetypes
import os
import re
import shutil
import subprocess
import tempfile
import threading
import time
import urllib.error
import urllib.parse
import urllib.request
import uuid
from http import HTTPStatus
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Any

ROOT_DIR = Path(__file__).resolve().parent
CONFIG_PATH = ROOT_DIR / "ig_config.json"
EXPORTS_DIR = ROOT_DIR / "exports"

DEFAULT_CONFIG: dict[str, Any] = {
    "ig_user_id": "",
    "access_token": "",
    "api_version": "v21.0",
    "share_to_feed": True,
    "save_local_copy": True,
    "ffmpeg_path": "",
    "cached_username": "",
}

# In-memory background job tracker for live UI progress updates
JOBS_LOCK = threading.Lock()
JOBS: dict[str, dict[str, Any]] = {}


def load_config() -> dict[str, Any]:
    cfg = dict(DEFAULT_CONFIG)
    if CONFIG_PATH.exists():
        try:
            with CONFIG_PATH.open("r", encoding="utf-8") as f:
                stored = json.load(f)
            if isinstance(stored, dict):
                cfg.update(stored)
        except Exception as exc:
            print(f"[warn] Could not read {CONFIG_PATH.name}: {exc}")

    # Environment variables can override empty config values
    if not cfg.get("ig_user_id") and os.environ.get("IG_USER_ID"):
        cfg["ig_user_id"] = os.environ["IG_USER_ID"].strip()
    if not cfg.get("access_token") and os.environ.get("IG_ACCESS_TOKEN"):
        cfg["access_token"] = os.environ["IG_ACCESS_TOKEN"].strip()
    if not cfg.get("ffmpeg_path") and os.environ.get("FFMPEG_PATH"):
        cfg["ffmpeg_path"] = os.environ["FFMPEG_PATH"].strip()
    return cfg


def save_config(updates: dict[str, Any]) -> dict[str, Any]:
    cfg = load_config()
    for key in DEFAULT_CONFIG:
        if key in updates:
            val = updates[key]
            # Don't overwrite existing token if UI sent blank placeholder
            if key == "access_token" and val == "__KEEP__":
                continue
            cfg[key] = val.strip() if isinstance(val, str) else val

    with CONFIG_PATH.open("w", encoding="utf-8") as f:
        json.dump(cfg, f, indent=2)
    return cfg


def find_ffmpeg(custom_path: str = "") -> str | None:
    """Locate ffmpeg executable from config, PATH, or common Windows install paths."""
    candidates: list[str] = []
    if custom_path:
        candidates.append(custom_path)

    which_path = shutil.which("ffmpeg")
    if which_path:
        candidates.append(which_path)

    # Common Windows install paths (WinGet, Chocolatey, Scoop, manual)
    local_app_data = os.environ.get("LOCALAPPDATA", "")
    user_profile = os.environ.get("USERPROFILE", "")
    common_paths = [
        r"C:\ffmpeg\bin\ffmpeg.exe",
        r"C:\Program Files\ffmpeg\bin\ffmpeg.exe",
        r"C:\ProgramData\chocolatey\bin\ffmpeg.exe",
        os.path.join(user_profile, "scoop", "shims", "ffmpeg.exe"),
    ]
    candidates.extend(common_paths)

    if local_app_data:
        winget_pkg = Path(local_app_data) / "Microsoft" / "WinGet" / "Packages"
        if winget_pkg.exists():
            for match in winget_pkg.glob("*FFmpeg*/*/bin/ffmpeg.exe"):
                candidates.append(str(match))
            for match in winget_pkg.glob("*FFmpeg*/*/*/bin/ffmpeg.exe"):
                candidates.append(str(match))

    for cand in candidates:
        if cand and Path(cand).is_file():
            return str(Path(cand))
    return None


def safe_filename(name: str, default_stem: str = "medbank_reel") -> str:
    stem = Path(name or default_stem).stem
    cleaned = re.sub(r"[^a-zA-Z0-9._-]+", "_", stem).strip("._-")
    return cleaned or default_stem


def transcode_to_instagram_mp4(
    input_path: Path, output_path: Path, ffmpeg_bin: str
) -> None:
    """
    Convert browser-recorded video (.webm or .mp4) to strict Instagram Reels specs:
    - 1080x1920 (9:16), yuv420p, H.264 High profile, 30 fps CFR
    - AAC stereo audio @ 48kHz, 128 kbps
    - +faststart moov atom at front for instant streaming & Meta ingestion
    """
    cmd = [
        ffmpeg_bin,
        "-y",
        "-i",
        str(input_path),
        "-vf",
        "scale=1080:1920:force_original_aspect_ratio=decrease,"
        "pad=1080:1920:(ow-iw)/2:(oh-ih)/2:color=black,"
        "format=yuv420p",
        "-r",
        "30",
        "-c:v",
        "libx264",
        "-profile:v",
        "high",
        "-level",
        "4.1",
        "-preset",
        "veryfast",
        "-crf",
        "20",
        "-maxrate",
        "8M",
        "-bufsize",
        "12M",
        "-c:a",
        "aac",
        "-b:a",
        "128k",
        "-ar",
        "48000",
        "-ac",
        "2",
        "-movflags",
        "+faststart",
        str(output_path),
    ]
    proc = subprocess.run(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    if proc.returncode != 0 or not output_path.exists() or output_path.stat().st_size == 0:
        tail = "\n".join(proc.stderr.splitlines()[-12:])
        raise RuntimeError(f"FFmpeg conversion failed:\n{tail}")


def graph_request(
    method: str,
    url: str,
    params: dict[str, Any] | None = None,
    data: bytes | None = None,
    headers: dict[str, str] | None = None,
    timeout: int = 120,
) -> dict[str, Any]:
    """Perform an HTTP request to Meta Graph / Rupload endpoints and parse JSON."""
    req_headers = {"User-Agent": "MedBankStudio/1.0"}
    if headers:
        req_headers.update(headers)

    body_bytes = data
    final_url = url
    if params:
        encoded = urllib.parse.urlencode(
            {k: v for k, v in params.items() if v is not None}
        )
        if method.upper() == "GET":
            sep = "&" if "?" in final_url else "?"
            final_url = f"{final_url}{sep}{encoded}"
        elif body_bytes is None:
            body_bytes = encoded.encode("utf-8")
            req_headers.setdefault(
                "Content-Type", "application/x-www-form-urlencoded"
            )

    req = urllib.request.Request(
        final_url, data=body_bytes, headers=req_headers, method=method.upper()
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            raw = resp.read().decode("utf-8", errors="replace")
            return json.loads(raw) if raw.strip() else {}
    except urllib.error.HTTPError as err:
        raw_err = err.read().decode("utf-8", errors="replace")
        detail = raw_err
        try:
            parsed = json.loads(raw_err)
            if isinstance(parsed, dict) and "error" in parsed:
                e = parsed["error"]
                msg = e.get("message", raw_err)
                subcode = e.get("error_subcode")
                user_msg = e.get("error_user_msg")
                detail = msg
                if user_msg and user_msg != msg:
                    detail += f" — {user_msg}"
                if subcode:
                    detail += f" (subcode {subcode})"
        except Exception:
            pass
        raise RuntimeError(f"Instagram API HTTP {err.code}: {detail}") from err
    except urllib.error.URLError as err:
        raise RuntimeError(f"Network error contacting Instagram API: {err.reason}") from err


def graph_base_url(access_token: str, api_ver: str) -> str:
    """Route IG-login tokens (IG...) to graph.instagram.com and Unified/FB tokens to graph.facebook.com."""
    host = "https://graph.instagram.com" if access_token.startswith("IG") else "https://graph.facebook.com"
    return f"{host}/{api_ver}"


def test_ig_connection(cfg: dict[str, Any]) -> dict[str, Any]:
    ig_user_id = cfg.get("ig_user_id", "").strip()
    token = cfg.get("access_token", "").strip()
    api_ver = cfg.get("api_version", "v21.0").strip() or "v21.0"

    if not ig_user_id or not token:
        raise ValueError("Please enter both your Instagram User ID and Access Token.")

    url = f"{graph_base_url(token, api_ver)}/{ig_user_id}"
    data = graph_request(
        "GET",
        url,
        params={
            "fields": "id,username,name,followers_count,media_count",
            "access_token": token,
        },
        timeout=30,
    )
    username = data.get("username") or data.get("name") or ig_user_id
    save_config({"cached_username": username})
    return data


def update_job(job_id: str, **fields: Any) -> None:
    with JOBS_LOCK:
        if job_id in JOBS:
            JOBS[job_id].update(fields)
            JOBS[job_id]["updated_at"] = time.time()


def run_publish_job(
    job_id: str,
    raw_video_bytes: bytes,
    source_ext: str,
    meta: dict[str, Any],
) -> None:
    """Background worker: FFmpeg transcode -> Resumable Upload -> Poll -> Publish."""
    tmp_dir = Path(tempfile.mkdtemp(prefix="medbank_reel_"))
    try:
        cfg = load_config()
        ig_user_id = cfg.get("ig_user_id", "").strip()
        access_token = cfg.get("access_token", "").strip()
        api_ver = cfg.get("api_version", "v21.0").strip() or "v21.0"

        if not ig_user_id or not access_token:
            raise RuntimeError(
                "Instagram API credentials are not configured. "
                "Click 'Instagram API Setup' to enter your IG User ID and Access Token."
            )

        caption = str(meta.get("caption", "")).strip()
        if len(caption) > 2200:
            caption = caption[:2197] + "..."
        share_to_feed = meta.get("share_to_feed", cfg.get("share_to_feed", True))
        save_local = meta.get("save_local_copy", cfg.get("save_local_copy", True))
        stem = safe_filename(str(meta.get("filename", "medbank_reel")))

        input_path = tmp_dir / f"raw_input.{source_ext}"
        input_path.write_bytes(raw_video_bytes)

        # Stage 1: Transcode to Instagram-native H.264 / AAC MP4 (skip if already WebCodecs IG MP4)
        ffmpeg_bin = find_ffmpeg(cfg.get("ffmpeg_path", ""))
        mp4_path = tmp_dir / f"{stem}.mp4"
        already_ig_mp4 = bool(meta.get("already_ig_mp4")) and source_ext.lower() == "mp4"

        if already_ig_mp4:
            update_job(
                job_id,
                stage="transcoding",
                progress=25,
                message="Using browser-encoded Instagram H.264 MP4...",
            )
            shutil.copy2(input_path, mp4_path)
        elif ffmpeg_bin:
            update_job(
                job_id,
                stage="transcoding",
                progress=25,
                message="Converting to Instagram-ready H.264 MP4 (FFmpeg)...",
            )
            transcode_to_instagram_mp4(input_path, mp4_path, ffmpeg_bin)
        elif source_ext.lower() == "mp4":
            update_job(
                job_id,
                stage="transcoding",
                progress=25,
                message="FFmpeg not found — uploading browser MP4 directly...",
            )
            shutil.copy2(input_path, mp4_path)
        else:
            raise RuntimeError(
                "FFmpeg is required to convert browser .webm recordings to Instagram .mp4. "
                "Install it in PowerShell with: winget install Gyan.FFmpeg  (then restart server.py)."
            )

        saved_local_path = ""
        if save_local:
            EXPORTS_DIR.mkdir(parents=True, exist_ok=True)
            timestamp = time.strftime("%Y%m%d_%H%M%S")
            dest = EXPORTS_DIR / f"{stem}_{timestamp}.mp4"
            shutil.copy2(mp4_path, dest)
            saved_local_path = str(dest)

        mp4_bytes = mp4_path.read_bytes()
        file_size = len(mp4_bytes)
        base_graph = graph_base_url(access_token, api_ver)

        # Stage 2: Initialize Resumable Upload Container
        # Pass upload_type=resumable in the query string and metadata (media_type, caption,
        # share_to_feed) in a JSON body so Meta preserves the Reel caption reliably!
        update_job(
            job_id,
            stage="initializing",
            progress=42,
            message="Creating Instagram Reel container...",
            local_file=saved_local_path,
        )
        init_url = f"{base_graph}/{ig_user_id}/media?upload_type=resumable"
        init_payload: dict[str, Any] = {
            "media_type": "REELS",
            "share_to_feed": bool(share_to_feed),
        }
        if caption:
            init_payload["caption"] = caption

        init_resp = graph_request(
            "POST",
            init_url,
            data=json.dumps(init_payload).encode("utf-8"),
            headers={
                "Authorization": f"Bearer {access_token}",
                "Content-Type": "application/json",
            },
            timeout=60,
        )
        container_id = init_resp.get("id")
        upload_uri = init_resp.get("uri") or (
            f"https://rupload.facebook.com/ig-api-upload/{api_ver}/{container_id}"
        )
        if not container_id:
            raise RuntimeError(f"Instagram did not return a container ID: {init_resp}")

        # Stage 3: Upload MP4 Binary to rupload.facebook.com
        update_job(
            job_id,
            stage="uploading",
            progress=60,
            message=f"Uploading MP4 ({file_size / (1024 * 1024):.1f} MB) directly to Instagram...",
            container_id=container_id,
        )
        graph_request(
            "POST",
            upload_uri,
            data=mp4_bytes,
            headers={
                "Authorization": f"OAuth {access_token}",
                "offset": "0",
                "file_size": str(file_size),
                "Content-Type": "application/octet-stream",
            },
            timeout=300,
        )

        # Stage 4: Poll Processing Status until FINISHED
        update_job(
            job_id,
            stage="processing",
            progress=76,
            message="Instagram is processing your Reel...",
        )
        status_url = f"{base_graph}/{container_id}"
        max_attempts = 45
        for attempt in range(max_attempts):
            st = graph_request(
                "GET",
                status_url,
                params={
                    "fields": "status_code,status",
                    "access_token": access_token,
                },
                timeout=30,
            )
            status_code = str(st.get("status_code", "")).upper()
            status_detail = st.get("status", "")
            if status_code == "FINISHED":
                break
            if status_code in ("ERROR", "EXPIRED"):
                raise RuntimeError(
                    f"Instagram failed to process the video ({status_code}): {status_detail}"
                )
            pct = min(90, 76 + int((attempt / max_attempts) * 14))
            update_job(
                job_id,
                progress=pct,
                message=f"Instagram is processing your Reel ({status_code or 'IN_PROGRESS'})...",
            )
            time.sleep(3)
        else:
            raise RuntimeError(
                "Timed out waiting for Instagram to finish processing the video."
            )

        # Stage 5: Publish Reel
        update_job(
            job_id,
            stage="publishing",
            progress=94,
            message="Publishing Reel live to Instagram...",
        )
        publish_url = f"{base_graph}/{ig_user_id}/media_publish"
        pub_resp = graph_request(
            "POST",
            publish_url,
            params={
                "creation_id": container_id,
                "access_token": access_token,
            },
            timeout=60,
        )
        media_id = pub_resp.get("id", "")

        # Optional: Fetch live permalink for instant viewing
        permalink = ""
        if media_id:
            try:
                link_resp = graph_request(
                    "GET",
                    f"{base_graph}/{media_id}",
                    params={"fields": "permalink", "access_token": access_token},
                    timeout=20,
                )
                permalink = link_resp.get("permalink", "")
            except Exception:
                pass

        update_job(
            job_id,
            status="done",
            stage="done",
            progress=100,
            message="Reel published live to Instagram!",
            media_id=media_id,
            permalink=permalink,
            local_file=saved_local_path,
        )
    except Exception as exc:
        update_job(
            job_id,
            status="error",
            stage="error",
            message=str(exc),
            error=str(exc),
        )
    finally:
        shutil.rmtree(tmp_dir, ignore_errors=True)


class MedBankHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, directory=str(ROOT_DIR), **kwargs)

    def log_message(self, format: str, *args: Any) -> None:
        # Keep console output clean & readable
        print(f"[MedBank] {self.address_string()} - {format % args}")

    def send_json(self, payload: dict[str, Any], status: int = 200) -> None:
        body = json.dumps(payload).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    def read_body(self) -> bytes:
        length = int(self.headers.get("Content-Length", "0") or "0")
        return self.rfile.read(length) if length > 0 else b""

    def read_json_body(self) -> dict[str, Any]:
        raw = self.read_body()
        if not raw:
            return {}
        return json.loads(raw.decode("utf-8"))

    def parse_meta_header(self) -> dict[str, Any]:
        encoded = self.headers.get("X-Reel-Meta", "")
        if not encoded:
            return {}
        try:
            raw = base64.b64decode(encoded).decode("utf-8")
            data = json.loads(raw)
            return data if isinstance(data, dict) else {}
        except Exception:
            return {}

    def do_GET(self) -> None:
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path

        if path == "/api/status":
            cfg = load_config()
            ffmpeg_bin = find_ffmpeg(cfg.get("ffmpeg_path", ""))
            self.send_json(
                {
                    "mode": "local",
                    "server": True,
                    "ffmpeg_available": bool(ffmpeg_bin),
                    "ffmpeg_path": ffmpeg_bin or "",
                    "ig_configured": bool(
                        cfg.get("ig_user_id") and cfg.get("access_token")
                    ),
                    "ig_username": cfg.get("cached_username", ""),
                    "api_version": cfg.get("api_version", "v21.0"),
                    "share_to_feed": bool(cfg.get("share_to_feed", True)),
                    "save_local_copy": bool(cfg.get("save_local_copy", True)),
                }
            )
            return

        if path == "/api/config":
            cfg = load_config()
            token = cfg.get("access_token", "")
            masked = (
                f"{token[:6]}...{token[-4:]}"
                if len(token) > 12
                else ("••••" if token else "")
            )
            self.send_json(
                {
                    "ig_user_id": cfg.get("ig_user_id", ""),
                    "has_token": bool(token),
                    "token_preview": masked,
                    "api_version": cfg.get("api_version", "v21.0"),
                    "share_to_feed": bool(cfg.get("share_to_feed", True)),
                    "save_local_copy": bool(cfg.get("save_local_copy", True)),
                    "ffmpeg_path": cfg.get("ffmpeg_path", ""),
                    "cached_username": cfg.get("cached_username", ""),
                }
            )
            return

        if path.startswith("/api/job/"):
            job_id = path.split("/api/job/", 1)[1].strip("/")
            with JOBS_LOCK:
                job = JOBS.get(job_id)
            if not job:
                self.send_json({"error": "Job not found"}, status=404)
                return
            self.send_json(job)
            return

        # Block direct static download of local credentials file
        if path.lower().endswith("ig_config.json"):
            self.send_json({"error": "Forbidden"}, status=403)
            return

        super().do_GET()

    def do_POST(self) -> None:
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path

        if path == "/api/config":
            try:
                body = self.read_json_body()
                cfg = save_config(body)
                self.send_json(
                    {
                        "ok": True,
                        "ig_configured": bool(
                            cfg.get("ig_user_id") and cfg.get("access_token")
                        ),
                        "ffmpeg_available": bool(
                            find_ffmpeg(cfg.get("ffmpeg_path", ""))
                        ),
                    }
                )
            except Exception as exc:
                self.send_json({"ok": False, "error": str(exc)}, status=400)
            return

        if path == "/api/test-connection":
            try:
                body = self.read_json_body()
                if body:
                    save_config(body)
                cfg = load_config()
                profile = test_ig_connection(cfg)
                self.send_json({"ok": True, "profile": profile})
            except Exception as exc:
                self.send_json({"ok": False, "error": str(exc)}, status=400)
            return

        if path == "/api/transcode":
            tmp_dir = Path(tempfile.mkdtemp(prefix="medbank_mp4_"))
            try:
                cfg = load_config()
                ffmpeg_bin = find_ffmpeg(cfg.get("ffmpeg_path", ""))
                if not ffmpeg_bin:
                    self.send_json(
                        {
                            "ok": False,
                            "error": (
                                "FFmpeg is not installed yet. Run "
                                "'winget install Gyan.FFmpeg' in PowerShell "
                                "and restart server.py to enable Instagram MP4 conversion."
                            ),
                        },
                        status=400,
                    )
                    return

                meta = self.parse_meta_header()
                raw_bytes = self.read_body()
                if not raw_bytes:
                    self.send_json({"ok": False, "error": "Empty video upload"}, status=400)
                    return

                content_type = self.headers.get("Content-Type", "video/webm").lower()
                src_ext = "mp4" if "mp4" in content_type else "webm"
                stem = safe_filename(str(meta.get("filename", "medbank_reel")))

                in_file = tmp_dir / f"in.{src_ext}"
                out_file = tmp_dir / f"{stem}.mp4"
                in_file.write_bytes(raw_bytes)

                transcode_to_instagram_mp4(in_file, out_file, ffmpeg_bin)
                mp4_bytes = out_file.read_bytes()

                if meta.get("save_local_copy", cfg.get("save_local_copy", True)):
                    EXPORTS_DIR.mkdir(parents=True, exist_ok=True)
                    ts = time.strftime("%Y%m%d_%H%M%S")
                    (EXPORTS_DIR / f"{stem}_{ts}.mp4").write_bytes(mp4_bytes)

                self.send_response(HTTPStatus.OK)
                self.send_header("Content-Type", "video/mp4")
                self.send_header("Content-Length", str(len(mp4_bytes)))
                self.send_header(
                    "Content-Disposition", f'attachment; filename="{stem}.mp4"'
                )
                self.send_header("Cache-Control", "no-store")
                self.end_headers()
                self.wfile.write(mp4_bytes)
            except Exception as exc:
                self.send_json({"ok": False, "error": str(exc)}, status=500)
            finally:
                shutil.rmtree(tmp_dir, ignore_errors=True)
            return

        if path == "/api/publish-reel":
            try:
                raw_bytes = self.read_body()
                if not raw_bytes:
                    self.send_json(
                        {"ok": False, "error": "No video data received."}, status=400
                    )
                    return

                meta = self.parse_meta_header()
                content_type = self.headers.get("Content-Type", "video/webm").lower()
                src_ext = "mp4" if "mp4" in content_type else "webm"

                job_id = uuid.uuid4().hex[:12]
                with JOBS_LOCK:
                    JOBS[job_id] = {
                        "id": job_id,
                        "status": "running",
                        "stage": "queued",
                        "progress": 10,
                        "message": "Video received — starting pipeline...",
                        "created_at": time.time(),
                        "updated_at": time.time(),
                    }

                worker = threading.Thread(
                    target=run_publish_job,
                    args=(job_id, raw_bytes, src_ext, meta),
                    daemon=True,
                )
                worker.start()

                self.send_json({"ok": True, "job_id": job_id}, status=202)
            except Exception as exc:
                self.send_json({"ok": False, "error": str(exc)}, status=500)
            return

        self.send_json({"error": "Not found"}, status=404)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="MedBank Studio Local Server + Direct Instagram Reel Publisher"
    )
    parser.add_argument("--host", default="127.0.0.1", help="Bind host (default: 127.0.0.1)")
    parser.add_argument("--port", type=int, default=8080, help="Bind port (default: 8080)")
    args = parser.parse_args()

    mimetypes.add_type("application/javascript", ".js")
    mimetypes.add_type("text/css", ".css")

    cfg = load_config()
    ffmpeg_bin = find_ffmpeg(cfg.get("ffmpeg_path", ""))
    ig_ready = bool(cfg.get("ig_user_id") and cfg.get("access_token"))

    print("=" * 64)
    print(f"  MedBank Studio Server running at http://{args.host}:{args.port}")
    print(f"  FFmpeg:        {'READY (' + ffmpeg_bin + ')' if ffmpeg_bin else 'NOT FOUND (run: winget install Gyan.FFmpeg)'}")
    print(f"  Instagram API: {'CONFIGURED' if ig_ready else 'NOT CONFIGURED (set up inside the Reel Studio UI)'}")
    print("  Press Ctrl+C to stop.")
    print("=" * 64)

    server = ThreadingHTTPServer((args.host, args.port), MedBankHandler)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down MedBank Studio Server...")
        server.server_close()


if __name__ == "__main__":
    main()
