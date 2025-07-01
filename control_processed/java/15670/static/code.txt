@Benchmark
  public int iter(IterState state)
  {
    ImmutableBitmap bitmap = state.bitmap;
    return iter(bitmap);
  }