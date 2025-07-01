private void processRows(
      IncrementalIndex<?> index,
      BitmapFactory bitmapFactory,
      List<IncrementalIndex.DimensionDesc> dimensions
  )
  {
    int rowNum = 0;
    for (IncrementalIndexRow row : index.getFacts().persistIterable()) {
      final Object[] dims = row.getDims();

      for (IncrementalIndex.DimensionDesc dimension : dimensions) {
        final int dimIndex = dimension.getIndex();
        DimensionAccessor accessor = accessors.get(dimension.getName());

        // Add 'null' to the dimension's dictionary.
        if (dimIndex >= dims.length || dims[dimIndex] == null) {
          accessor.indexer.processRowValsToUnsortedEncodedKeyComponent(null, true);
          continue;
        }
        final ColumnCapabilities capabilities = dimension.getCapabilities();

        if (capabilities.hasBitmapIndexes()) {
          final MutableBitmap[] bitmapIndexes = accessor.invertedIndexes;
          final DimensionIndexer indexer = accessor.indexer;
          indexer.fillBitmapsFromUnsortedEncodedKeyComponent(dims[dimIndex], rowNum, bitmapIndexes, bitmapFactory);
        }
      }
      ++rowNum;
    }
  }