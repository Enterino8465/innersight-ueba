# Shared Pydantic v2 models consumed by BOTH the API and the worker.
# This is the single source of truth for data shapes that cross service boundaries.
# Exports: CanonicalEvent, UserDayFeatureRecord, EmbeddingPayload, EvalMetrics.
# Installed as a path dependency in both apps/api and apps/worker pyproject.toml.
