public static Frame transpose(Frame src){
    if(src.numRows() != (int)src.numRows())
      throw H2O.unimpl();
    int nchunks = Math.max(1,src.numCols()/10000);
    long [] espc = new long[nchunks+1];
    int rpc = (src.numCols() / nchunks);
    int rem = (src.numCols() % nchunks);
    Arrays.fill(espc, rpc);
    for (int i = 0; i < rem; ++i) ++espc[i];
    long sum = 0;
    for (int i = 0; i < espc.length; ++i) {
      long s = espc[i];
      espc[i] = sum;
      sum += s;
    }
    Key key = Vec.newKey();
    int rowLayout = Vec.ESPC.rowLayout(key,espc);
    return transpose(src, new Frame(new Vec(key,rowLayout).makeZeros((int)src.numRows())));
  }