@Override boolean set_impl(int i, long l) {
    if( _ds   != null ) return set_impl(i,(double)l);
    if(_sparseLen != _len){ // sparse?
      int idx = Arrays.binarySearch(_id,0, _sparseLen,i);
      if(idx >= 0)i = idx;
      else cancel_sparse(); // for now don't bother setting the sparse value
    }
    _ms.set(i,l);
    _xs.set(i,0);
    if(_missing != null)_missing.clear(i);
    _naCnt = -1;
    return true;
  }