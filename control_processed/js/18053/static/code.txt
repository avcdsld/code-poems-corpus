function mulScalar(v, k, dst) {
  dst = dst || new VecType(3);

  dst[0] = v[0] * k;
  dst[1] = v[1] * k;
  dst[2] = v[2] * k;

  return dst;
}