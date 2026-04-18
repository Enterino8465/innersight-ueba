# Week 4 model — GraphSAGE on per-user-day ego HeteroData.
# Implements the Model protocol from blueprint §8.
# Self-supervised training via link prediction (positive = observed edges,
# negative = randomly sampled non-edges).
# embed(): returns 128-dim user node embedding after message passing.
# Vectors stored in Qdrant collection user_day_graphsage_v1 (dim=128, cosine).
# Must beat Node2Vec on eval harness before we move to R-GCN.
