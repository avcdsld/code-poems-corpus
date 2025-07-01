private static int parseNanos(String value) throws ParseException {
    int result = 0;
    for (int i = 0; i < 9; ++i) {
      result = result * 10;
      if (i < value.length()) {
        if (value.charAt(i) < '0' || value.charAt(i) > '9') {
          throw new ParseException("Invalid nanoseconds.", 0);
        }
        result += value.charAt(i) - '0';
      }
    }
    return result;
  }