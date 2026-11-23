import { handleUpload } from "@vercel/blob/client";
import { verifyPasscode } from "./_ig.js";

export async function POST(request) {
  let body;
  try {
    body = await request.json();
  } catch (e) {
    return Response.json({ error: "Invalid JSON body." }, { status: 400 });
  }

  try {
    const jsonResponse = await handleUpload({
      body,
      request,
      onBeforeGenerateToken: async (_pathname, clientPayload) => {
        let parsed = {};
        if (clientPayload) {
          try {
            parsed = JSON.parse(clientPayload);
          } catch (e) {}
        }
        verifyPasscode(request, parsed.passcode || "");

        return {
          allowedContentTypes: ["video/mp4"],
          maximumSizeInBytes: 100 * 1024 * 1024, // 100 MB max per Reel
          addRandomSuffix: true,
        };
      },
      onUploadCompleted: async () => {
        // Cleanup happens in /api/ig-publish once Instagram finishes ingesting the video
      },
    });

    return Response.json(jsonResponse);
  } catch (err) {
    return Response.json(
      { error: err.message || "Failed to authorize Vercel Blob upload." },
      { status: err.status || 400 }
    );
  }
}
