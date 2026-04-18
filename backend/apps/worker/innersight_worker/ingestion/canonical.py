# Canonical event dataclass — the normalized intermediate form between raw CSVs and the DB.
# Fields: ts (datetime), user_id (str), action (str), src_entity (str),
#   dst_entity (str), attrs (dict).
# Action values must be from the vocabulary in blueprint §6.
# Used by cert_parser.py (producer) and the DB writer in cli.py (consumer).
