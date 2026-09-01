import json

from eeg_isr.experiments.results import ExperimentResult


def test_experiment_result_save(tmp_path):
    result = ExperimentResult(
        experiment_id="baseline-001",
        model="SVM",
        metrics={"accuracy": 0.75, "f1": 0.72},
    )

    output = tmp_path / "metrics.json"
    result.save(output)

    data = json.loads(output.read_text(encoding="utf-8"))

    assert data["experiment_id"] == "baseline-001"
    assert data["metrics"]["accuracy"] == 0.75
