# Data Flow

raw .tar.bz2 archives
  -> extracted .set/.fdt (EEGLAB format)
  -> filtered .fif (bandpass 0.5-50Hz, thinking epochs only)
  -> feature vectors (bandpower + statistical features)
  -> scaled + K-best selected features
  -> train/test split (subject-aware)
  -> SVM classifier
  -> predictions -> metrics -> experiment result
