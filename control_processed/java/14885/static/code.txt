public static void main(String[] argv) throws Exception {
    SingleThreadBlockingQpsBenchmark bench = new SingleThreadBlockingQpsBenchmark();
    bench.setup();
    for  (int i = 0; i < 10000; i++) {
      bench.blockingUnary();
    }
    Thread.sleep(30000);
    bench.teardown();
    System.exit(0);
  }