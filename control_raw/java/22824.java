@Benchmark
  public Response buildAndQuery_fake() {
    return Feign.builder().client(fakeClient)
        .target(FeignTestInterface.class, "http://localhost").query();
  }