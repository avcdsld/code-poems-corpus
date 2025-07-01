function lockedCheck(from, to) {
  from = fis.file.wrap(from).realpath;
  to = fis.file.wrap(to).realpath;
  if (from === to) {
    return true;
  } else if (lockedMap[to]) {
    var prev = from;
    var msg = [];

    do {
      msg.unshift(prev);
      prev = lockedMap[prev];
    } while (prev);

    prev && msg.unshift(prev);
    msg.push(to);
    return msg;
  }
  return false;
}