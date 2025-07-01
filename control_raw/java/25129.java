synchronized public static String calcNextUniqueModelId(String desc) {
    StringBuilder sb = new StringBuilder();
    sb.append(desc).append("_model_");

    // Append user agent string if we can figure it out.
    String source = ServletUtils.getUserAgent();
    if (source != null) {
      StringBuilder ua = new StringBuilder();

      if (source.contains("Safari")) {
        ua.append("safari");
      }
      else if (source.contains("Python")) {
        ua.append("python");
      }
      else {
        for (int i = 0; i < source.length(); i++) {
          char c = source.charAt(i);
          if (c >= 'a' && c <= 'z') {
            ua.append(c);
            continue;
          } else if (c >= 'A' && c <= 'Z') {
            ua.append(c);
            continue;
          }
          break;
        }
      }

      if (ua.toString().length() > 0) {
        sb.append(ua.toString()).append("_");
      }
    }

    // REST API needs some refactoring to avoid burning lots of extra numbers.
    //
    // I actually tried only doing the addAndGet only for POST requests (and junk UUID otherwise),
    // but that didn't eliminate the gaps.
    long n = nextModelNum.addAndGet(1);
    sb.append(Long.toString(CLUSTER_ID)).append("_").append(Long.toString(n));

    return sb.toString();
  }