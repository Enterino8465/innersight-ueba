# GNNExplainer wrapper — post-hoc explainability for any trained GNN.
# explain(model, hetero_data, user_node_id) → edge_mask (float tensor) + subgraph.
# Edge mask values indicate each edge's contribution to the anomaly score.
# Output is serialised as JSON and stored in MinIO; served by /api/suspects/:id/explain.
