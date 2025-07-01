public void addNum(double d) {
    if( isUUID() || isString() ) { addNA(); return; }
    boolean predicate = _sparseNA ? !Double.isNaN(d) : isSparseZero()?d != 0:true;
    if(predicate) {
      if(_ms != null) {
        if((long)d == d){
          addNum((long)d,0);
          return;
        }
        switch_to_doubles();
      }
      //if ds not big enough
      if(_sparseLen == _ds.length ) {
        append2slowd();
        // call addNum again since append2slowd might have flipped to sparse
        addNum(d);
        assert _sparseLen <= _len;
        return;
      }
      if(_id != null)_id[_sparseLen] = _len;
      _ds[_sparseLen] = d;
      _sparseLen++;
    }
    _len++;
    assert _sparseLen <= _len;
  }