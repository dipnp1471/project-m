import { put } from "@vercel/blob";
import { generateClientTokenFromReadWriteToken } from "@vercel/blob/client";
import { getEnvConfig, verifyPasscode } from "./_ig.js";

function sanitizeFilename(name) {
  const cleaned = String(name || "medbank_reel.mp4")
    .replace(/[^a-zA-Z0-9._-]+/g, "_")
    .replace(/^[._-]+|[._-]+$/g, "");
  return cleaned.endsWith(".mp4") ? cleaned : `${cleaned || "medbank_reel"}.mp4`;
}

export async function POST(request) {
  try {
    verifyPasscode(request);
    const { blobToken } = getEnvConfig();
    if (!blobToken) {
      return Response.json(
        {
          ok: false,
          error:
            "BLOB_READ_WRITE_TOKEN is missing. Enable a Public Vercel Blob Store in your Vercel project's Storage tab and redeploy.",
        },
        { status: 400 }
      );
    }

    const url = new URL(request.url);
    const mode = url.searchParams.get("mode") || "direct";

    // Mode 1: Mint a scoped client token for >4 MB direct browser PUT to blob.vercel-storage.com
    if (mode === "token") {
      const body = await request.json();
      const filename = sanitizeFilename(body?.filename);
      const pathname = `reels/${filename}`;

      const clientToken = await generateClientTokenFromReadWriteToken({
        token: blobToken,
        pathname,
        allowedContentTypes: ["video/mp4"],
        maximumSizeInBytes: 100 * 1024 * 1024,
        addRandomSuffix: true,
      });

      return Response.json({
        ok: true,
        clientToken,
        pathname,
        uploadUrl: `https://blob.vercel-storage.com/${encodeURI(pathname)}`,
      });
    }

    // Mode 2 (Default for <=4 MB): Direct server-side put() — zero CORS, zero client SDK
    const filename = sanitizeFilename(url.searchParams.get("filename"));
    const pathname = `reels/${filename}`;
    const arrayBuffer = await request.arrayBuffer();
    if (!arrayBuffer || arrayBuffer.byteLength === 0) {
      return Response.json(
        { ok: false, error: "Empty MP4 upload received." },
        { status: 400 }
      );
    }

    const blob = await put(pathname, arrayBuffer, {
      access: "public",
      contentType: "video/mp4",
      addRandomSuffix: true,
      token: blobToken,
    });

    return Response.json({ ok: true, url: blob.url, pathname: blob.pathname });
  } catch (err) {
    return Response.json(
      { ok: false, error: err.message || "Failed to upload MP4 to Vercel Blob." },
      { status: err.status || 500 }
    );
  }
}
