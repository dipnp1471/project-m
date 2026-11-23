import { getEnvConfig } from "./_ig.js";

export async function GET() {
  const cfg = getEnvConfig();
  return Response.json(
    {
      mode: "vercel",
      server: true,
      blob_configured: Boolean(cfg.blobToken),
      ig_configured: Boolean(cfg.igUserId && cfg.accessToken),
      passcode_required: Boolean(cfg.adminPasscode),
      api_version: cfg.apiVersion,
      ig_username: (process.env.IG_USERNAME || "").trim(),
      share_to_feed: true,
    },
    {
      headers: { "Cache-Control": "no-store" },
    }
  );
}
