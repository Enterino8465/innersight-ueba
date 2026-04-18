FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim AS builder

WORKDIR /app
ENV UV_COMPILE_BYTECODE=1 UV_LINK_MODE=copy

COPY pyproject.toml .
RUN uv sync --no-install-project --no-dev

COPY innersight_worker/ innersight_worker/
RUN uv sync --no-dev

FROM python:3.12-slim AS runtime

WORKDIR /app

COPY --from=builder /app/.venv /app/.venv
COPY --from=builder /app/innersight_worker /app/innersight_worker

ENV PATH="/app/.venv/bin:$PATH"

ENTRYPOINT ["innersight-worker"]
CMD ["hello"]
