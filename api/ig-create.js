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

    const body = await request.json();
    const videoUrl = String(body?.video_url || "").trim();
    if (!videoUrl || !videoUrl.startsWith("https://")) {
      return Response.json(
        { ok: false, error: "A valid HTTPS video_url is required." },
        { status: 400 }
      );
    }

    let caption = String(body?.caption || "").trim();
    if (caption.length > 2200) {
      caption = caption.slice(0, 2197) + "...";
    }
    const shareToFeed = body?.share_to_feed !== false;

    const base = graphBaseUrl(accessToken, apiVersion);
    const payload = {
      media_type: "REELS",
      video_url: videoUrl,
      share_to_feed: shareToFeed,
    };
    if (caption) {
      payload.caption = caption;
    }

    // Sending JSON body with video_url + Authorization Bearer ensures Meta reliably preserves caption
    const resp = await metaFetch(`${base}/${igUserId}/media`, {
      method: "POST",
      headers: {
        Authorization: `Bearer ${accessToken}`,
        "Content-Type": "application/json",
      },
      body: JSON.stringify(payload),
    });

    if (!resp.id) {
      throw new Error(`Instagram did not return a container ID: ${JSON.stringify(resp)}`);
    }

    return Response.json({
      ok: true,
      container_id: resp.id,
      caption_chars: caption.length,
    });
  } catch (err) {
    return Response.json(
      { ok: false, error: err.message || "Failed to create Instagram Reel container." },
      { status: err.status || 500 }
    );
  }
}
