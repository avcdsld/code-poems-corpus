public Chunk compress() {
    Chunk res = compress2();
    byte type = type();
    assert _vec == null ||  // Various testing scenarios do not set a Vec
      type == _vec._type || // Equal types
      // Allow all-bad Chunks in any type of Vec
      type == Vec.T_BAD ||
      // Specifically allow the NewChunk to be a numeric type (better be all
      // ints) and the selected Vec type an categorical - whose String mapping
      // may not be set yet.
      (type==Vec.T_NUM && _vec._type==Vec.T_CAT) ||
      // Another one: numeric Chunk and Time Vec (which will turn into all longs/zeros/nans Chunks)
      (type==Vec.T_NUM && _vec._type == Vec.T_TIME && !res.hasFloat())
      : "NewChunk has type "+Vec.TYPE_STR[type]+", but the Vec is of type "+_vec.get_type_str();
    assert _len == res._len : "NewChunk has length "+_len+", compressed Chunk has "+res._len;
    // Force everything to null after compress to free up the memory.  Seems
    // like a non-issue in the land of GC, but the NewChunk *should* be dead
    // after this, but might drag on.  The arrays are large, and during a big
    // Parse there's lots and lots of them... so free early just in case a GC
    // happens before the drag-time on the NewChunk finishes.
    _id = null;
    _xs = null;
    _ds = null;
    _ms = null;
    _is = null;
    _ss = null;
    return res;
  }