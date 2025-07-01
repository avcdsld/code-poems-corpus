function weight(kernel, bandwidth, x_0, x_i) {
  const arg = (x_i - x_0) / bandwidth;
  return kernel(arg);
}