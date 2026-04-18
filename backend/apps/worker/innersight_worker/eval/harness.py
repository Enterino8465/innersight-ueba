# Evaluation harness — the source of truth for model quality (blueprint §10).
# evaluate(model, split="test") → writes one JSON file to ml/experiments/<timestamp>__<model>.json.
# Computes: auc, pr_auc, precision_at_10, precision_at_50, recall_at_50,
#   alerts_per_1k_users_per_day, time_to_detect_days (p50/p90), per-scenario breakdowns.
# compare_to_baseline(): loads last merged baseline from ml/experiments/ and emits deltas.
# CI gate: fails if auc or precision_at_50 drops >0.02 vs baseline.
