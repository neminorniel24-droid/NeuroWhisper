"""Sanity check that the LICENSE file is present."""
import os

def test_license_exists():
    assert os.path.exists("LICENSE")
