# Graph service — fetches and formats ego-graph data for the API.
# get_graph_snapshot(user_id, date): loads the .pt file from MinIO for the given
#   user+date, converts PyG HeteroData into Cytoscape-ready JSON
#   (nodes with type/label, edges with relation/weight).
