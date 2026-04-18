# SQLAlchemy ORM models — mirror the Postgres schema in blueprint §4.
# Tables: User, Event, Label, UserDayFeatures, Investigation, AuthUser, AuditLog.
# Every column name and type matches the CREATE TABLE statements exactly.
# Relationships: User.supervisor (self-ref), Investigation.suspect_user, etc.
