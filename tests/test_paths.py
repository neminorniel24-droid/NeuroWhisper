from pathlib import Path

from eeg_isr.utils.paths import (
    configs_dir,
    data_dir,
    features_dir,
    models_dir,
    project_root,
    results_dir,
)


def test_project_root_exists():
    assert project_root().is_dir()


def test_project_root_contains_project_files():
    root = project_root()

    assert (root / "pyproject.toml").is_file()
    assert (root / "README.md").is_file()


def test_project_directories_are_path_objects():
    assert isinstance(data_dir(), Path)
    assert isinstance(features_dir(), Path)
    assert isinstance(models_dir(), Path)
    assert isinstance(results_dir(), Path)
    assert isinstance(configs_dir(), Path)
