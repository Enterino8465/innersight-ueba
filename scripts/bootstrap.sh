#!/usr/bin/env bash
# One-command dev setup.
# Checks prerequisites (Docker, Python 3.12, uv, pnpm).
# Copies .env.example → .env if not present.
# Runs `docker compose -f infra/compose/docker-compose.dev.yml up -d`.
# Runs Alembic migrations. Creates Qdrant collections from collections.yml.
# Prints access URLs for api (:8000), web (:5173), MinIO console (:9001).
