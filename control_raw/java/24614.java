public static Header[] parseHttpHeaders(final String headers) {
    if (headers == null || headers.length() == 0) {
      return null;
    }

    final String[] headerArray = headers.split(HEADER_ELEMENT_DELIMITER);
    final List<Header> headerList = new ArrayList<>(headerArray.length);
    for (int i = 0; i < headerArray.length; i++) {
      final String headerPair = headerArray[i];
      final int index = headerPair.indexOf(HEADER_NAME_VALUE_DELIMITER);
      if (index != -1) {
        headerList.add(new BasicHeader(headerPair.substring(0, index),
            headerPair.substring(index + 1)));
      }

    }
    return headerList.toArray(new BasicHeader[0]);
  }