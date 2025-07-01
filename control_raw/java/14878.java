@Benchmark
  @BenchmarkMode(Mode.SampleTime)
  @OutputTimeUnit(TimeUnit.NANOSECONDS)
  public byte[] messageEncodePlain() {
    return Status.MESSAGE_KEY.toBytes("Unexpected RST in stream");
  }