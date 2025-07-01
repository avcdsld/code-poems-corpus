function negate(v, dst) {
  dst = dst || new VecType(3);

  dst[0] = -v[0];
  dst[1] = -v[1];
  dst[2] = -v[2];

  return dst;
}