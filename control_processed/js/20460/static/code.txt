function isFileLike(v) {
  return Buffer.isBuffer(v) ||
    typeof v === 'object' &&
    typeof v.pipe === 'function' &&
    v.readable !== false;
}