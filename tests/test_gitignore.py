"""Ensure large data directories are excluded from version control."""
def test_gitignore_excludes_data():
    with open(".gitignore") as f:
        content = f.read()
    assert "venv/" in content
    assert "files/Data/" in content
