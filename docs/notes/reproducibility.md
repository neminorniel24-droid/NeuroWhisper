# Reproducibility

- Fixed random_state/seed used across train/test splits and model init
- Config-driven runs: same config.yaml -> same experiment result
- Raw/filtered/feature data excluded from git; regenerable via workflows/
