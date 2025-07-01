public static void main(String[] argv) throws Exception {
    StreamingResponseBandwidthBenchmark bench = new StreamingResponseBandwidthBenchmark();
    bench.setup();
    Thread.sleep(30000);
    bench.teardown();
    System.exit(0);
  }