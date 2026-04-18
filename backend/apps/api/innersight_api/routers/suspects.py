# Suspect Discovery router — /api/suspects/* endpoints (blueprint §12).
# POST /api/suspects/{user_id}/neighbors — k-NN query against Qdrant;
#   returns ranked list of behaviorally similar users for a given date.
# GET  /api/suspects/{user_id}/explain   — GNNExplainer edge-mask result;
#   returns top-K contributing edges + node roles for explainability UI.
