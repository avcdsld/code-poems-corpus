public static String removeChar(String s, char c)
  {
    int pos = s.indexOf(c);
    if (pos < 0) {
      return s;
    }
    StringBuilder sb = new StringBuilder(s.length() - 1);
    int prevPos = 0;
    do {
      sb.append(s, prevPos, pos);
      prevPos = pos + 1;
      pos = s.indexOf(c, pos + 1);
    } while (pos > 0);
    sb.append(s, prevPos, s.length());
    return sb.toString();
  }