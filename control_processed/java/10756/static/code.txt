private static void embedDarkDotAtLeftBottomCorner(ByteMatrix matrix) throws WriterException {
    if (matrix.get(8, matrix.getHeight() - 8) == 0) {
      throw new WriterException();
    }
    matrix.set(8, matrix.getHeight() - 8, 1);
  }