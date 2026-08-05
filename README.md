# NeuroWhisper

Imagined speech recognition from EEG signals — decoding silently-imagined words directly from brain activity, without any vocalization.

## Overview

NeuroWhisper is a research project exploring whether a person's *imagined* speech (thinking a word without saying it out loud) can be decoded purely from EEG signals using machine learning. This is a step toward assistive communication technology for people who cannot speak due to conditions like ALS, locked-in syndrome, or paralysis — where language and cognition remain intact, but the motor pathway to physically speak is impaired.

This project is simulation-based: rather than building custom EEG hardware, it uses a public research-grade EEG dataset to validate the decoding approach first, before considering any hardware implementation.

## Dataset

This project uses the **[Kara One database](https://www.cs.toronto.edu/~complingweb/data/karaOne/karaOne.html)** — a public EEG dataset recorded from 14 participants, using 62-channel EEG, capturing brain activity across several speech-related phonemes and words (e.g. *pat*, *pot*, *knew*, *gnaw*) in multiple states: resting, hearing the stimulus, imagining speaking it, and actually speaking it. This project focuses specifically on the **imagined speech ("thinking")** epochs.

## Pipeline

1. **Download** — Fetch raw EEG recordings for all subjects.
2. **Feature extraction** — Filter and extract the imagined-speech ("thinking") epochs from the raw signal, saving processed data.
3. **Classification** — Train and evaluate machine learning classifiers to predict which word/phoneme was imagined, purely from EEG features.

This pipeline is built on top of the open-source [EEG-Imagined-speech-recognition](https://github.com/AshrithSagar/EEG-Imagined-speech-recognition) framework (MIT licensed), configured here specifically for the Kara One dataset and imagined-speech decoding.

## Setup

```bash
git clone https://github.com/neminorniel24-droid/NeuroWhisper.git
cd NeuroWhisper
python3.13 -m venv venv
source venv/bin/activate
pip install -e .
```

Copy the config template and set your local data paths:
```bash
cp config-template.yaml config.yaml
```

## Usage

```bash
# Download the dataset
python3 workflows/download-karaone.py

# Extract imagined-speech features
python3 workflows/features-karaone.py

# Train a baseline classifier
python3 workflows/flatten-classifier.py
```

## Research Direction

- Baseline classification accuracy using classical ML (SVM, Random Forest) on imagined-speech EEG features.
- Comparison against deep learning approaches (CNN/LSTM) on the same features.
- Exploring reduced-channel subsets to evaluate feasibility for low-cost, few-channel EEG hardware in future work.

## Motivation

Most imagined-speech BCI research relies on expensive, research-grade, high-channel-count EEG systems. This project explores the problem using open data and open tools first, as groundwork toward evaluating whether accessible, low-cost approaches could eventually support real assistive communication use cases.

## Acknowledgements

- [The Kara One Database](https://www.cs.toronto.edu/~complingweb/data/karaOne/karaOne.html) — Toronto Computational Linguistics Group
- [EEG-Imagined-speech-recognition](https://github.com/AshrithSagar/EEG-Imagined-speech-recognition) by Ashrith Sagar Yedlapalli (MIT License)

## License

MIT
