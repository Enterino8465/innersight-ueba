# Loads a small slice of canonical events into Postgres for local testing.
# Useful before the full CERT dataset is downloaded.
# Inserts ~50 synthetic users and ~500 events covering all action types in §6.
# Also seeds one AuthUser (admin role) for API testing.
# Run with: python scripts/seed_db.py
