# Qdrant sync — upserts embeddings from user_day_features into the correct collection.
# upsert(collection_name, user_id, date, vector, payload) → upserts one point.
# sync_date(model_name, date) → batch-upserts all users for a given date.
# Payload shape matches blueprint §5: user_id, date, anomaly_score, department,
#   scenario_label, model_version, computed_at.
# HNSW params: m=16, ef_construct=200 (set at collection creation, not here).
