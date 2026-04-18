# Auth router (week 6).
# POST /api/auth/login   — validates email+password, issues JWT pair.
# POST /api/auth/refresh — validates refresh token, issues new access token.
# POST /api/auth/logout  — invalidates refresh token (adds to Redis blocklist).
