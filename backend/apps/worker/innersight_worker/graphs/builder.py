# Per-user-day ego-graph builder.
# build_ego_graph(user_id, date) → PyG HeteroData.
# Queries events table for the given user+date, creates nodes for each entity
# (User, Host, File, URL, USBDevice, EmailAddress) and edges per the ontology in §7.
# 2-hop from the User node, capped at 500 neighbors per edge type (random sample beyond).
# Serialises the HeteroData to MinIO at s3://innersight/graphs/{version}/{YYYY/MM/DD}/{user_id}.pt
