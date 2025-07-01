private ValFrame fast_table(Vec v1, int ncols, String colname) {
    if (ncols != 1 || !v1.isInt()) return null;
    long spanl = (long) v1.max() - (long) v1.min() + 1;
    if (spanl > 1000000) return null; // Cap at decent array size, for performance

    // First fast-pass counting
    AstTable.FastCnt fastCnt = new AstTable.FastCnt((long) v1.min(), (int) spanl).doAll(v1);
    final long cnts[] = fastCnt._cnts;
    final long minVal = fastCnt._min;

    // Second pass to build the result frame, skipping zeros
    Vec dataLayoutVec = Vec.makeCon(0, cnts.length);
    Frame fr = new MRTask() {
      @Override
      public void map(Chunk cs[], NewChunk nc0, NewChunk nc1) {
        final Chunk c = cs[0];
        for (int i = 0; i < c._len; ++i) {
          int idx = (int) (i + c.start());
          if (cnts[idx] > 0) {
            nc0.addNum(idx + minVal);
            nc1.addNum(cnts[idx]);
          }
        }
      }
    }.doAll(new byte[]{Vec.T_NUM, Vec.T_NUM}, dataLayoutVec).outputFrame(new String[]{colname, "Count"},
        new String[][]{v1.domain(), null});
    dataLayoutVec.remove();
    return new ValFrame(fr);
  }