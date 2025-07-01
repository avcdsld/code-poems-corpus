public static HyperLogLogCollector makeCollector(ByteBuffer buffer)
  {
    int remaining = buffer.remaining();
    if (remaining % 3 == 0 || remaining == 1027) {
      return new VersionZeroHyperLogLogCollector(buffer);
    } else {
      return new VersionOneHyperLogLogCollector(buffer);
    }
  }