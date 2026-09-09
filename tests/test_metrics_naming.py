"""Sanity check standard metric names used across this project's docs/results."""

EXPECTED_METRICS = {"accuracy", "precision", "recall", "f1"}

def test_accuracy_in_metrics():
    assert "accuracy" in EXPECTED_METRICS

def test_metric_count():
    assert len(EXPECTED_METRICS) == 4
