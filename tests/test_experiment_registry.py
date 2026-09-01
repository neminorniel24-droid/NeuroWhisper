import pytest

from eeg_isr.experiments.registry import (
    ExperimentDefinition,
    ExperimentRegistry,
)


def test_registry():
    registry = ExperimentRegistry()

    experiment = ExperimentDefinition(
        experiment_id="baseline-001",
        description="Baseline SVM",
        model="SVM",
    )

    registry.register(experiment)

    assert registry.get("baseline-001") == experiment
    assert len(registry.list()) == 1


def test_duplicate_experiment_is_rejected():
    registry = ExperimentRegistry()

    experiment = ExperimentDefinition(
        experiment_id="baseline-001",
        description="Baseline SVM",
        model="SVM",
    )

    registry.register(experiment)

    with pytest.raises(ValueError):
        registry.register(experiment)
