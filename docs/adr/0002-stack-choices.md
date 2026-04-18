# ADR-0002: Stack Choices

## Status
Accepted

## Decision
Backend: Python 3.12, FastAPI, Pydantic v2, SQLAlchemy 2.x + Alembic, Qdrant, Redis, MinIO.
ML: PyTorch + PyTorch Geometric, scikit-learn, MLflow.
Dev: Docker Compose, GitHub Actions, ruff + mypy + eslint + tsc.

## Consequences
Stack is locked for v1.0. Changes require a new ADR.
