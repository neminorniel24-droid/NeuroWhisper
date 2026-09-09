# features/ package

- band_config.py — configurable EEG frequency bands (delta/theta/alpha/beta/gamma)
- bandpower.py — computes power per band per channel
- pipeline.py — orchestrates the full feature extraction flow
- scaling.py — leakage-safe feature scaling (fit on train only)
- selection.py — leakage-safe K-best feature selection
- statistical.py — statistical feature descriptors (mean/var/etc.)
