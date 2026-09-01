"""Registry for reproducible NeuroWhisper experiments."""

from dataclasses import dataclass


@dataclass(frozen=True)
class ExperimentDefinition:
    """Metadata describing an experiment."""

    experiment_id: str
    description: str
    model: str


class ExperimentRegistry:
    """In-memory registry of experiment definitions."""

    def __init__(self) -> None:
        self._experiments: dict[str, ExperimentDefinition] = {}

    def register(self, experiment: ExperimentDefinition) -> None:
        """Register an experiment."""
        if experiment.experiment_id in self._experiments:
            raise ValueError(
                f"Experiment already registered: {experiment.experiment_id}"
            )

        self._experiments[experiment.experiment_id] = experiment

    def get(self, experiment_id: str) -> ExperimentDefinition:
        """Retrieve an experiment definition."""
        return self._experiments[experiment_id]

    def list(self) -> list[ExperimentDefinition]:
        """Return registered experiments."""
        return list(self._experiments.values())
