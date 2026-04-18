# Week 5 primary model — Relational GCN (R-GCN) on heterogeneous ego graphs.
# Implements the Model protocol from blueprint §8.
# Handles multiple edge types (blueprint §7) with type-specific weight matrices.
# Training: self-supervised link prediction + optional contrastive loss.
# embed(): returns 128-dim user embedding.
# Vectors stored in Qdrant collection user_day_rgcn_v1 (dim=128, cosine).
# This is the final production model — must beat GraphSAGE on eval harness.
