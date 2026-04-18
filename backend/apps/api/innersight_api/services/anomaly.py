# Anomaly service — pure business logic, no HTTP concerns.
# query_top_anomalies(date, limit): fetches top-N users by anomaly_score from user_day_features.
# query_user_history(user_id, from_date, to_date): returns daily anomaly scores as a timeline.
# write_audit_log(actor_id, action, target, payload): inserts a row into audit_log.
