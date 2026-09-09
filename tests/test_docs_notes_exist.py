"""Sanity check that key project documentation notes exist."""
import os

EXPECTED = [
    "docs/notes/dataset-notes.md",
    "docs/notes/pipeline-notes.md",
    "docs/notes/research-direction.md",
    "docs/notes/roadmap.md",
]

def test_notes_exist():
    for path in EXPECTED:
        assert os.path.exists(path), f"missing {path}"
