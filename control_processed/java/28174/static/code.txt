public Filter label(@Nonnull String label) {
    Preconditions.checkNotNull(label);
    return new SimpleFilter(RowFilter.newBuilder().setApplyLabelTransformer(label).build());
  }