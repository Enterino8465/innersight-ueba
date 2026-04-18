# Investigations router — /api/investigations/* endpoints (blueprint §12).
# GET  /api/investigations          — paginated list, filterable by status.
# POST /api/investigations          — create new investigation for a suspect+date.
# GET  /api/investigations/{id}     — fetch single investigation.
# POST /api/investigations/{id}/notes — append a timestamped analyst note.
# POST /api/investigations/{id}/close — set status to closed or dismissed.
# Every mutation writes to audit_log via services.anomaly.
