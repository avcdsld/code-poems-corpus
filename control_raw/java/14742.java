@CheckReturnValue
  public static byte[][] toRawSerializedHeaders(byte[][] http2Headers) {
    for (int i = 0; i < http2Headers.length; i += 2) {
      byte[] key = http2Headers[i];
      byte[] value = http2Headers[i + 1];
      if (endsWith(key, binaryHeaderSuffixBytes)) {
        // Binary header
        for (int idx = 0; idx < value.length; idx++) {
          if (value[idx] == (byte) ',') {
            return serializeHeadersWithCommasInBin(http2Headers, i);
          }
        }
        byte[] decodedVal = BaseEncoding.base64().decode(new String(value, US_ASCII));
        http2Headers[i + 1] = decodedVal;
      } else {
        // Non-binary header
        // Nothing to do, the value is already in the right place.
      }
    }
    return http2Headers;
  }