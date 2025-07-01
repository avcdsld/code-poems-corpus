@Benchmark
  public Object blockingUnary() throws Exception {
    return ClientCalls.blockingUnaryCall(
        channels[0].newCall(unaryMethod, CallOptions.DEFAULT), Unpooled.EMPTY_BUFFER);
  }