"""Standardized experiment result representation."""

from dataclasses import asdict, dataclass, field
from pathlib import Path
import json
from typing import Any


@dataclass
class ExperimentResult:
    """Metrics and metadata produced by one experiment."""

    experiment_id: str
    model: str
    metrics: dict[str, float]
    parameters: dict[str, Any] = field(default_factory=dict)

    def save(self, path: str | Path) -> None:
        """Save results as JSON."""
        output = Path(path)
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(
            json.dumps(asdict(self), indent=2),
            encoding="utf-8",
        )
