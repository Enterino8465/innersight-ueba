# Week 1 baseline model — scikit-learn IsolationForest.
# Implements the Model protocol from blueprint §8.
# fit(): trains on the 15-feature vectors from user_day_features for a date range.
# embed(): returns the raw anomaly_score (1D) — not a true embedding but satisfies the protocol.
# Vectors stored in Qdrant collection user_day_iforest_v1 (dim=15, cosine).
# This is intentionally simple — the point is to establish a measurable baseline.
