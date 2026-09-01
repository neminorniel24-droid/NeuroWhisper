"""Project path utilities.

All paths are resolved relative to the NeuroWhisper project root rather
than being tied to a particular user's filesystem.
"""

from pathlib import Path


def project_root() -> Path:
    """Return the root directory of the NeuroWhisper project."""
    return Path(__file__).resolve().parents[3]


def data_dir() -> Path:
    """Return the project's data directory."""
    return project_root() / "files" / "Data"


def features_dir() -> Path:
    """Return the project's feature directory."""
    return project_root() / "files" / "Features"


def models_dir() -> Path:
    """Return the project's model directory."""
    return project_root() / "files" / "Models"


def results_dir() -> Path:
    """Return the project's results directory."""
    return project_root() / "results"


def configs_dir() -> Path:
    """Return the project's configuration directory."""
    return project_root() / "configs"
