# EEG-ISR Package Architecture

The `eeg_isr` package is organized into functional layers.

## Layers

- `data/`
  - Dataset loading
  - Dataset metadata
  - Data validation
  - Dataset-specific adapters

- `preprocessing/`
  - EEG filtering
  - Epoch extraction
  - Artifact handling
  - Signal preprocessing

- `features/`
  - Feature extraction
  - Spectral features
  - Statistical features
  - Spatial features
  - Feature selection

- `models/`
  - Classical machine-learning models
  - Deep-learning models
  - Model factories

- `evaluation/`
  - Metrics
  - Cross-validation
  - Confusion matrices
  - Statistical comparisons

- `experiments/`
  - Experiment configuration
  - Experiment execution
  - Experiment tracking

- `visualization/`
  - EEG visualizations
  - Feature visualizations
  - Model/evaluation plots

- `utils/`
  - Shared utilities
  - Reproducibility
  - Logging
  - Paths and configuration helpers

## Migration strategy

Existing modules in the package root are intentionally preserved during
the initial architecture migration. Functionality will be moved into the
appropriate layer incrementally, with tests added before each migration.

This avoids breaking existing workflows while improving maintainability.
