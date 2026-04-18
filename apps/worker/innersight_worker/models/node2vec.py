# Week 3 baseline model — Node2Vec on the daily org graph.
# Implements the Model protocol from blueprint §8.
# Uses PyTorch Geometric's Node2Vec with random walks + skip-gram.
# embed(): returns 64-dim user embedding from the trained lookup table.
# Vectors stored in Qdrant collection user_day_node2vec_v1 (dim=64, cosine).
# Must beat IsolationForest on the eval harness before we move to GNN.
