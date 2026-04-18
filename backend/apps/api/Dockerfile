# Multi-stage Dockerfile for the FastAPI service.
# Stage 1 (builder): installs Python deps with uv into a venv.
# Stage 2 (runtime): copies venv + source; runs uvicorn on port 8000.
# Lives on both 'internal' and 'web' Docker networks (see §3).
