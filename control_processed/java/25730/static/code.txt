public int[] diffCols(int[] filterThese) {
    HashSet<Integer> filter = new HashSet<>();
    for(int i:filterThese)filter.add(i);
    ArrayList<Integer> res = new ArrayList<>();
    for(int i=0;i<_cols.length;++i) {
      if( _cols[i]._ignored || _cols[i]._response || filter.contains(i) ) continue;
      res.add(i);
    }
    return intListToA(res);
  }