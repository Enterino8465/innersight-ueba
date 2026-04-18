# Daily organisation-wide graph builder.
# build_org_graph(date) → PyG HeteroData spanning ALL users for that day.
# Used for pre-training Node2Vec and the initial GraphSAGE self-supervised pass.
# Merges all per-user ego-graphs, deduplicates shared entity nodes (e.g. shared hosts),
# and stores the result to MinIO at s3://innersight/graphs/org/{YYYY/MM/DD}/org.pt.
