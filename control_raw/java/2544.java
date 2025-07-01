private static String getHttpOnlyCookieHeader(Cookie cookie) {
    NewCookie newCookie = new NewCookie(cookie.getName(), cookie.getValue(),
      cookie.getPath(), cookie.getDomain(), cookie.getVersion(),
      cookie.getComment(), cookie.getMaxAge(), cookie.getSecure());
    return newCookie + "; HttpOnly";
  }