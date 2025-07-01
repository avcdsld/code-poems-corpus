public void insertRecord(long recordPointer, long keyPrefix, boolean prefixIsNull) {
    if (!hasSpaceForAnotherRecord()) {
      throw new IllegalStateException("There is no space for new record");
    }
    if (prefixIsNull && radixSortSupport != null) {
      // Swap forward a non-null record to make room for this one at the beginning of the array.
      array.set(pos, array.get(nullBoundaryPos));
      pos++;
      array.set(pos, array.get(nullBoundaryPos + 1));
      pos++;
      // Place this record in the vacated position.
      array.set(nullBoundaryPos, recordPointer);
      nullBoundaryPos++;
      array.set(nullBoundaryPos, keyPrefix);
      nullBoundaryPos++;
    } else {
      array.set(pos, recordPointer);
      pos++;
      array.set(pos, keyPrefix);
      pos++;
    }
  }