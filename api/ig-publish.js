import { del } from "@vercel/blob";
import { getEnvConfig, graphBaseUrl, metaFetch, verifyPasscode } from "./_ig.js";

async function cleanupBlob(blobUrl) {
  if (!blobUrl || !blobUrl.includes("vercel-storage.com")) return;
  try {
    await del(blobUrl);
  } catch (e) {
    // Non-fatal: ignore cleanup errors
  }
}

export async function POST(request) {
  let blobUrl = "";
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
    const containerId = String(body?.container_id || "").trim();
    blobUrl = String(body?.blob_url || "").trim();

    if (!containerId) {
      return Response.json(
        { ok: false, error: "container_id is required." },
        { status: 400 }
      );
    }

    const base = graphBaseUrl(accessToken, apiVersion);

    // 1. Check container processing status
    const statusParams = new URLSearchParams({
      fields: "status_code,status",
      access_token: accessToken,
    });
    const st = await metaFetch(`${base}/${containerId}?${statusParams.toString()}`);
    const statusCode = String(st.status_code || "").toUpperCase();

    if (statusCode === "ERROR" || statusCode === "EXPIRED") {
      await cleanupBlob(blobUrl);
      return Response.json(
        {
          ok: false,
          status: "error",
          status_code: statusCode,
          error: `Instagram failed to process the video (${statusCode}): ${st.status || "Unknown error"}`,
        },
        { status: 400 }
      );
    }

    if (statusCode !== "FINISHED" && statusCode !== "PUBLISHED") {
      return Response.json({
        ok: true,
        status: "processing",
        status_code: statusCode || "IN_PROGRESS",
      });
    }

    // 2. Publish container live to Instagram
    const pubResp = await metaFetch(`${base}/${igUserId}/media_publish`, {
      method: "POST",
      headers: {
        Authorization: `Bearer ${accessToken}`,
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ creation_id: containerId }),
    });
    const mediaId = pubResp.id || "";

    // 3. Fetch live Reel permalink
    let permalink = "";
    if (mediaId) {
      try {
        const linkParams = new URLSearchParams({
          fields: "permalink",
          access_token: accessToken,
        });
        const linkResp = await metaFetch(`${base}/${mediaId}?${linkParams.toString()}`);
        permalink = linkResp.permalink || "";
      } catch (e) {}
    }

    // 4. Delete temporary MP4 from Vercel Blob to keep storage clean
    await cleanupBlob(blobUrl);

    return Response.json({
      ok: true,
      status: "done",
      media_id: mediaId,
      permalink,
    });
  } catch (err) {
    return Response.json(
      { ok: false, error: err.message || "Failed to publish Reel." },
      { status: err.status || 500 }
    );
  }
}
