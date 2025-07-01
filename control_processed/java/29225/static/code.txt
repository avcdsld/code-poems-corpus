@InternalApi
  public static Row create(ByteString key, List<RowCell> cells) {
    return new AutoValue_Row(key, cells);
  }