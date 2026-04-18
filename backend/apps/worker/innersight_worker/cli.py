# Typer CLI — single entrypoint for all batch jobs (blueprint §11).
# Subcommands: ingest, build-graphs, extract-features, train, infer, evaluate, sync-qdrant.
# Every command is idempotent and accepts --dry-run to preview without writing.
# Scheduled daily chain: ingest → build-graphs → extract-features → infer → sync-qdrant → evaluate.
