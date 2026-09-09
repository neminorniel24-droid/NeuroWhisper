# Known Bugs Found & Fixed

1. Path duplication in karaone.py load_raw_data() — glob result was
   already absolute, joining it with data_dir again broke file lookup.
2. features.py / features/ package name collision — old FeatureFunctions
   class was shadowed by the new features/ package, breaking feis.py import.
   Fixed by moving old file to legacy_features.py and re-exporting.
3. Archive extraction preserved original absolute researcher paths
   (p/spoclab/users/szhao/...) instead of flat subject folders — required
   a flattening step post-extraction.
