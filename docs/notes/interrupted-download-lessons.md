# Lessons on Long-Running Downloads in WSL

- Laptop lid close / sleep interrupts WSL background processes
- tmux protects against terminal close, not full system sleep
- Corrupted archives fail silently until extraction/read time
- Always verify with `bzip2 -tv` before trusting a downloaded archive
- Fix: disable sleep-on-lid-close while long downloads run
