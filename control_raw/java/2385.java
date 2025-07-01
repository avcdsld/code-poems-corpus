public static CountMinSketch readFrom(byte[] bytes) throws IOException {
    try (InputStream in = new ByteArrayInputStream(bytes)) {
      return readFrom(in);
    }
  }