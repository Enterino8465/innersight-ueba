# Thin Qdrant wrapper — all vector operations for the API layer.
# knn_search(collection, query_vector, k, filters): runs Qdrant search, returns hits with payload.
# get_point(collection, point_id): fetch a single embedding by user_id+date.
# Used by suspects router to power the k-NN neighbor and explain endpoints.
