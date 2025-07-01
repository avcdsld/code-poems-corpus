public R startOpen(@Nonnull T start) {
    this.start = Preconditions.checkNotNull(start, "Start can't be null");
    this.startBound = BoundType.OPEN;
    return thisT();
  }