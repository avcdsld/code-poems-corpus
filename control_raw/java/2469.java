public static void readFully(ReadableByteChannel channel, ByteBuffer dst) throws IOException {
    int expected = dst.remaining();
    while (dst.hasRemaining()) {
      if (channel.read(dst) < 0) {
        throw new EOFException(String.format("Not enough bytes in channel (expected %d).",
          expected));
      }
    }
  }