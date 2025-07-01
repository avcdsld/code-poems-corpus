public static int indexOfControlOrNonAscii(String input) {
    for (int i = 0, length = input.length(); i < length; i++) {
      char c = input.charAt(i);
      if (c <= '\u001f' || c >= '\u007f') {
        return i;
      }
    }
    return -1;
  }