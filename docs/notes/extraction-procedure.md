# Archive Extraction Procedure

1. Extract .tar.bz2 into subject-named folder
2. Locate nested original path (p/spoclab/.../data/<subject>)
3. Move contents up to the subject folder root
4. Move set_files/ contents up as well
5. Remove now-empty nested path
6. Verify subject folder has a top-level .set file before proceeding
