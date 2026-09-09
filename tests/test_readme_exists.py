"""Sanity check that core project documentation exists."""
import os

def test_readme_exists():
    assert os.path.exists("README.md")

def test_changelog_exists():
    assert os.path.exists("CHANGELOG.md")
