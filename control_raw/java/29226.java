public List<RowCell> getCells(@Nonnull String family) {
    Preconditions.checkNotNull(family, "family");

    int start = getFirst(family, null);
    if (start < 0) {
      return ImmutableList.of();
    }

    int end = getLast(family, null, start);

    return getCells().subList(start, end + 1);
  }