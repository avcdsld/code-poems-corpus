function XYZToLngLat([x, y, z]) {
  const lat = Math.atan2(z, Math.sqrt(x * x + y * y));
  const lng = Math.atan2(y, x);

  return [lng * RADIAN_TO_DEGREE, lat * RADIAN_TO_DEGREE];
}