# CERT r4.2 CSV parser — reads the raw source files and emits CanonicalEvent objects.
# Handles all six log types: logon.csv, device.csv, file.csv, http.csv, email.csv, psychometric.csv.
# Maps each row to the canonical event vocabulary in blueprint §6.
# Skips already-ingested rows (idempotent via event deduplication on ts+user_id+action).
