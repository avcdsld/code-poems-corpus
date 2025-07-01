@Override
  public final ColumnarArray getArray(int rowId) {
    if (isNullAt(rowId)) return null;
    return new ColumnarArray(arrayData(), getArrayOffset(rowId), getArrayLength(rowId));
  }