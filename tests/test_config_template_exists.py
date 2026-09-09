"""Sanity check that the config template ships with the repo."""
import os

def test_config_template_exists():
    assert os.path.exists("config-template.yaml")
