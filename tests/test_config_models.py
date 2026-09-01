import pytest

from eeg_isr.utils.config_loader import load_yaml_config
from eeg_isr.utils.config_models import (
    ClassifierConfig,
    ProjectConfig,
    build_project_config,
)


def test_build_project_config():
    config = load_yaml_config("config.yaml")
    project = build_project_config(config)

    assert isinstance(project, ProjectConfig)
    assert isinstance(project.classifier, ClassifierConfig)
    assert project.classifier.random_state == 42
    assert project.karaone.subjects == "all"


def test_invalid_test_size():
    with pytest.raises(ValueError):
        ClassifierConfig(test_size=2.0)
