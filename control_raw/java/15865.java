public static long parseLong(Object val)
  {
    if (val instanceof String) {
      return Long.parseLong((String) val);
    } else if (val instanceof Number) {
      return ((Number) val).longValue();
    } else {
      if (val == null) {
        throw new NullPointerException("Input is null");
      } else {
        throw new ISE("Unknown type [%s]", val.getClass());
      }
    }
  }