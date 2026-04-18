# Health and metrics router.
# GET /healthz  — checks DB connectivity and Qdrant reachability; returns {"status":"ok"}.
# GET /metrics  — Prometheus text exposition (via prometheus-client).
