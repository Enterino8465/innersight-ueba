-- Extensions and role setup. Run once on first container start.
-- Full schema is managed by Alembic migrations in apps/api/innersight_api/alembic/.

CREATE EXTENSION IF NOT EXISTS pgcrypto;
CREATE EXTENSION IF NOT EXISTS pg_trgm;
