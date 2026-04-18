# ADR-0001: Frontend Never Talks to the Database

## Status
Accepted

## Context
The frontend (React) must never have a direct connection to Postgres, Qdrant, Redis, or MinIO.

## Decision
Enforced at the Docker network level: the web service is on the 'web' network only;
all databases are on the 'internal' network only. Only the API service bridges both.

## Consequences
Even if a developer accidentally writes a direct DB call in frontend code, the packets
have nowhere to go. The contract is structural, not just cultural.
