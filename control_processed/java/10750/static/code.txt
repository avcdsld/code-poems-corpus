static void embedTypeInfo(ErrorCorrectionLevel ecLevel, int maskPattern, ByteMatrix matrix)
      throws WriterException {
    BitArray typeInfoBits = new BitArray();
    makeTypeInfoBits(ecLevel, maskPattern, typeInfoBits);

    for (int i = 0; i < typeInfoBits.getSize(); ++i) {
      // Place bits in LSB to MSB order.  LSB (least significant bit) is the last value in
      // "typeInfoBits".
      boolean bit = typeInfoBits.get(typeInfoBits.getSize() - 1 - i);

      // Type info bits at the left top corner. See 8.9 of JISX0510:2004 (p.46).
      int[] coordinates = TYPE_INFO_COORDINATES[i];
      int x1 = coordinates[0];
      int y1 = coordinates[1];
      matrix.set(x1, y1, bit);

      if (i < 8) {
        // Right top corner.
        int x2 = matrix.getWidth() - i - 1;
        int y2 = 8;
        matrix.set(x2, y2, bit);
      } else {
        // Left bottom corner.
        int x2 = 8;
        int y2 = matrix.getHeight() - 7 + (i - 8);
        matrix.set(x2, y2, bit);
      }
    }
  }