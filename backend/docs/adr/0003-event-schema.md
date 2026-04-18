# ADR-0003: Canonical Event Vocabulary

## Status
Accepted

## Decision
All log sources normalise into the events table using the action vocabulary in blueprint §6.
New sources add new action strings; they never overload existing ones.
Changing the vocabulary requires a DB migration and a bump to this ADR.

## Consequences
Consistent querying and graph construction across all CERT log types.
