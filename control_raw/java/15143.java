@Benchmark
  public void pingPong(AdditionalCounters counters) throws Exception {
    record.set(true);
    // No need to do anything, just sleep here.
    Thread.sleep(1001);
    record.set(false);
  }