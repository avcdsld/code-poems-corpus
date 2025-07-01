private static String getCharacter(Table table, int code) {
    switch (table) {
      case UPPER:
        return UPPER_TABLE[code];
      case LOWER:
        return LOWER_TABLE[code];
      case MIXED:
        return MIXED_TABLE[code];
      case PUNCT:
        return PUNCT_TABLE[code];
      case DIGIT:
        return DIGIT_TABLE[code];
      default:
        // Should not reach here.
        throw new IllegalStateException("Bad table");
    }
  }