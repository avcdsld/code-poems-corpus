public static String[][] unboxStringArrays(Collection<String[]> coll) {
    return coll.toArray(new String[coll.size()][]);
  }