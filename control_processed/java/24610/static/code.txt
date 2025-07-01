private static String stripSingleDoubleQuote(String input) {
    if (StringUtils.isEmpty(input)) {
      return input;
    }

    if (input.startsWith(SINGLE_QUOTE_STRING)
        || input.startsWith(DOUBLE_QUOTE_STRING)) {
      input = input.substring(1);
    }

    if (input.endsWith(SINGLE_QUOTE_STRING)
        || input.endsWith(DOUBLE_QUOTE_STRING)) {
      input = input.substring(0, input.length() - 1);
    }

    return input;
  }