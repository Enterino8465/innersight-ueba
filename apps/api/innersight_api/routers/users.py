# Users router — all /api/users/* endpoints (blueprint §12).
# GET /api/users                       — paginated user list, filterable by dept/query.
# GET /api/users/{user_id}             — full user profile.
# GET /api/users/{user_id}/history     — anomaly score per day over a date range.
# GET /api/users/top-anomalies         — top N highest-scoring users for a given date.
# GET /api/users/{user_id}/graph       — Cytoscape-ready ego-graph snapshot for a date.
