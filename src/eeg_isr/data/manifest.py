"""Dataset manifest structures."""

from dataclasses import asdict, dataclass
from pathlib import Path
import json


@dataclass(frozen=True)
class DatasetRecord:
    """Description of one dataset subject/file."""

    subject: str
    path: str
    exists: bool


@dataclass
class DatasetManifest:
    """Collection of dataset records."""

    dataset_name: str
    records: list[DatasetRecord]

    @property
    def subject_count(self) -> int:
        """Return the number of unique subjects."""
        return len({record.subject for record in self.records})

    def to_json(self, path: str | Path) -> None:
        """Save the manifest as JSON."""
        output = Path(path)
        output.parent.mkdir(parents=True, exist_ok=True)

        payload = {
            "dataset_name": self.dataset_name,
            "records": [asdict(record) for record in self.records],
        }

        output.write_text(
            json.dumps(payload, indent=2),
            encoding="utf-8",
        )
