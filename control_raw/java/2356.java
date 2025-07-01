public static int[] toJavaIntArray(ColumnarArray array) {
    for (int i = 0; i < array.numElements(); i++) {
      if (array.isNullAt(i)) {
        throw new RuntimeException("Cannot handle NULL values.");
      }
    }
    return array.toIntArray();
  }