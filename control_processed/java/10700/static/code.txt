private static int determineConsecutiveBinaryCount(String msg, int startpos, Charset encoding)
      throws WriterException {
    CharsetEncoder encoder = encoding.newEncoder();
    int len = msg.length();
    int idx = startpos;
    while (idx < len) {
      char ch = msg.charAt(idx);
      int numericCount = 0;

      while (numericCount < 13 && isDigit(ch)) {
        numericCount++;
        //textCount++;
        int i = idx + numericCount;
        if (i >= len) {
          break;
        }
        ch = msg.charAt(i);
      }
      if (numericCount >= 13) {
        return idx - startpos;
      }
      ch = msg.charAt(idx);

      if (!encoder.canEncode(ch)) {
        throw new WriterException("Non-encodable character detected: " + ch + " (Unicode: " + (int) ch + ')');
      }
      idx++;
    }
    return idx - startpos;
  }