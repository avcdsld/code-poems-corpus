public static Optional<Cookie> getCookieFromRequest(final String cookieName, final HttpServletRequest request) {
        val cookies = request.getCookies();
        if (cookies == null) {
            return Optional.empty();
        }
        return Arrays.stream(cookies).filter(c -> c.getName().equalsIgnoreCase(cookieName)).findFirst();
    }