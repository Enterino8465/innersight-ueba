# InnerSight UEBA

Insider threat and compromised-credential detection using heterogeneous Graph Neural Networks.

## Quick start
```bash
./scripts/bootstrap.sh        # start full stack
./scripts/download_cert.sh    # fetch CERT r4.2 dataset
worker ingest --source cert   # parse CSVs into Postgres
```

## Structure
- `apps/api/`    — FastAPI backend (the only DB client)
- `apps/worker/` — ingestion + ML training/inference CLI
- `infra/`       — Docker Compose, Postgres init, Qdrant collections
- `ml/`          — model configs, experiment results, notebooks
- `packages/`    — shared Pydantic schemas
- `docs/`        — ADRs, model card, eval report, final report
- `scripts/`     — bootstrap, dataset download, seed data

See `docs/adr/` for key architectural decisions.
