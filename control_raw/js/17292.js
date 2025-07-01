function lock(from, to) {
  from = fis.file.wrap(from).realpath;
  to = fis.file.wrap(to).realpath;

  lockedMap[to] = from;
}