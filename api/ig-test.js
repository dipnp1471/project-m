import { getEnvConfig, graphBaseUrl, metaFetch, verifyPasscode } from "./_ig.js";

export async function POST(request) {
  try {
    verifyPasscode(request);
    const { igUserId, accessToken, apiVersion } = getEnvConfig();

    if (!igUserId || !accessToken) {
      return Response.json(
        {
          ok: false,
          error:
            "Missing IG_USER_ID or IG_ACCESS_TOKEN in Vercel Environment Variables.",
        },
        { status: 400 }
      );
    }

    const base = graphBaseUrl(accessToken, apiVersion);
    const params = new URLSearchParams({
      fields: "id,username,name,followers_count,media_count",
      access_token: accessToken,
    });
    const profile = await metaFetch(`${base}/${igUserId}?${params.toString()}`);

    return Response.json({ ok: true, profile });
  } catch (err) {
    return Response.json(
      { ok: false, error: err.message || "Connection test failed." },
      { status: err.status || 400 }
    );
  }
}
