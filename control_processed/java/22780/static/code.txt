public static String encodeReserved(String value, FragmentType type, Charset charset) {
    /* value is encoded, we need to split it up and skip the parts that are already encoded */
    Matcher matcher = PCT_ENCODED_PATTERN.matcher(value);

    if (!matcher.find()) {
      return encodeChunk(value, type, charset);
    }

    int length = value.length();
    StringBuilder encoded = new StringBuilder(length + 8);
    int index = 0;
    do {
      /* split out the value before the encoded value */
      String before = value.substring(index, matcher.start());

      /* encode it */
      encoded.append(encodeChunk(before, type, charset));

      /* append the encoded value */
      encoded.append(matcher.group());

      /* update the string search index */
      index = matcher.end();
    } while (matcher.find());

    /* append the rest of the string */
    String tail = value.substring(index, length);
    encoded.append(encodeChunk(tail, type, charset));
    return encoded.toString();
  }