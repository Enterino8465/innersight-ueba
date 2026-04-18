# Integration tests — runs against real Postgres + Qdrant via docker-compose.test.yml.
# Uses pytest-asyncio + httpx.AsyncClient pointed at a live FastAPI instance.
# Covers every endpoint in §12: happy path + error cases (404, 422, 401).
