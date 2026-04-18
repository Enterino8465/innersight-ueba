# Async SQLAlchemy engine + session factory.
# Creates AsyncEngine from DATABASE_URL, exposes AsyncSessionLocal
# used by deps.get_db() to yield per-request sessions.
