#!/usr/bin/env bash
# Downloads CERT Insider Threat r4.2 dataset from CMU KiltHub.
# Verifies SHA-256 checksum after download.
# Extracts to storage/data/cert-r42/ (gitignored).
# Prints next step: run `worker ingest --source cert`.
