/**
 * Shared helpers for MedBank Studio Vercel Serverless Functions.
 * Files prefixed with "_" in api/ are NOT exposed as public endpoints by Vercel.
 */

export function getEnvConfig() {
  const igUserId = (process.env.IG_USER_ID || "").trim();
  const accessToken = (process.env.IG_ACCESS_TOKEN || "").trim();
  const apiVersion = (process.env.IG_API_VERSION || "v21.0").trim() || "v21.0";
  const adminPasscode = (process.env.ADMIN_PASSCODE || "").trim();
  const blobToken = (process.env.BLOB_READ_WRITE_TOKEN || "").trim();

  return {
    igUserId,
    accessToken,
    apiVersion,
    adminPasscode,
    blobToken,
  };
}

export function verifyPasscode(request, providedOverride = "") {
  const { adminPasscode } = getEnvConfig();
  if (!adminPasscode) return; // Passcode optional if env var not set
  const headerCode = (request.headers.get("x-admin-passcode") || "").trim();
  const provided = (providedOverride || headerCode).trim();
  if (!provided || provided !== adminPasscode) {
    const err = new Error(
      "Invalid or missing publishing passcode. Open 'Instagram API Setup' and enter your Vercel ADMIN_PASSCODE."
    );
    err.status = 401;
    throw err;
  }
}

export function graphBaseUrl(accessToken, apiVersion) {
  const host = accessToken.startsWith("IG")
    ? "https://graph.instagram.com"
    : "https://graph.facebook.com";
  return `${host}/${apiVersion}`;
}

export async function metaFetch(url, options = {}) {
  const resp = await fetch(url, options);
  const text = await resp.text();
  let data = {};
  try {
    data = text ? JSON.parse(text) : {};
  } catch (e) {
    data = { raw: text };
  }

  if (!resp.ok) {
    const e = data?.error;
    let detail = text;
    if (e) {
      detail = e.message || text;
      if (e.error_user_msg && e.error_user_msg !== detail) {
        detail += ` — ${e.error_user_msg}`;
      }
      if (e.error_subcode) {
        detail += ` (subcode ${e.error_subcode})`;
      }
    }
    const err = new Error(`Instagram API HTTP ${resp.status}: ${detail}`);
    err.status = resp.status >= 400 && resp.status < 500 ? 400 : 502;
    throw err;
  }
  return data;
}
