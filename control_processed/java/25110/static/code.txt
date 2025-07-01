@Override public final void initFromBytes () {
    _start = -1;  _cidx = -1;
    set_len(_mem.length>>3);
    assert _mem.length == _len <<3;
  }