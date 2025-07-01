public ValRow slice(int[] cols) {
    double[] ds = new double[cols.length];
    String[] ns = new String[cols.length];
    for (int i = 0; i < cols.length; ++i) {
      ds[i] = _ds[cols[i]];
      ns[i] = _names[cols[i]];
    }
    return new ValRow(ds, ns);
  }