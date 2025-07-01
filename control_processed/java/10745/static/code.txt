public void rotate180() {
    int width = getWidth();
    int height = getHeight();
    BitArray topRow = new BitArray(width);
    BitArray bottomRow = new BitArray(width);
    for (int i = 0; i < (height + 1) / 2; i++) {
      topRow = getRow(i, topRow);
      bottomRow = getRow(height - 1 - i, bottomRow);
      topRow.reverse();
      bottomRow.reverse();
      setRow(i, bottomRow);
      setRow(height - 1 - i, topRow);
    }
  }