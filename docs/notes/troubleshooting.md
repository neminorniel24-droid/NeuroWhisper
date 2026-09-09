# Troubleshooting Notes

## Corrupted archive on extraction
Symptom: bzip2 "Data integrity error"
Fix: delete the .tar.bz2 and re-run download-karaone.py; it skips already-valid files.

## Path duplication bug
Symptom: FileNotFoundError with a doubled path segment
Cause: joining an already-absolute glob result with the base dir again
Fix: use the glob result directly, not os.path.join with the same base dir.
