public static String concatenateForRewrite(
      final String base,
      final String encodedPath,
      @Nullable final String encodedQueryString
  )
  {
    // Query string and path are already encoded, no need for anything fancy beyond string concatenation.

    final StringBuilder url = new StringBuilder(base).append(encodedPath);

    if (encodedQueryString != null) {
      url.append("?").append(encodedQueryString);
    }

    return url.toString();
  }