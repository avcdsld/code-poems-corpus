public static byte[] unboxBytes(Collection<Byte> coll) {
    byte[] res = new byte[coll.size()];
    int i = 0;
    for (Byte elem : coll)
      res[i++] = elem;
    return res;
  }