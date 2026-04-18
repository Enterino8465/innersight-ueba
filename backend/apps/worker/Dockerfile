# Multi-stage Dockerfile for the worker service.
# Stage 1 (builder): installs Python deps (including PyTorch + PyG) with uv.
# Stage 2 (runtime): copies venv + source; default CMD runs the Typer CLI.
# Lives on 'internal' Docker network only — no web exposure.
# PyTorch image base recommended for GPU support; CPU-only for CI.
