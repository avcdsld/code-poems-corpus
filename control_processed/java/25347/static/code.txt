static boolean isZipDirectory(Key key) {
    Iced ice = DKV.getGet(key);
    if (ice == null) throw new H2OIllegalArgumentException("Missing data", "Did not find any data under " +
            "key " + key);
    ByteVec bv = (ByteVec) (ice instanceof ByteVec ? ice : ((Frame) ice).vecs()[0]);

    return isZipDirectory(bv);
  }