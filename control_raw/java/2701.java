@Override
  public UnsafeRow copy() {
    UnsafeRow rowCopy = new UnsafeRow(numFields);
    final byte[] rowDataCopy = new byte[sizeInBytes];
    Platform.copyMemory(
      baseObject,
      baseOffset,
      rowDataCopy,
      Platform.BYTE_ARRAY_OFFSET,
      sizeInBytes
    );
    rowCopy.pointTo(rowDataCopy, Platform.BYTE_ARRAY_OFFSET, sizeInBytes);
    return rowCopy;
  }