# Data Integrity Checklist

Before running feature extraction, verify:
1. All 14 subject .tar.bz2 archives pass `bzip2 -tv`
2. Each subject folder has a top-level .set + .fdt pair (post-flatten)
3. No 0-byte files in any subject folder
4. filtered_data_dir is empty or intentionally being overwritten
