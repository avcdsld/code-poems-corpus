public static Collection<String> getRequestedScopes(final HttpServletRequest context) {
        val map = getRequestParameters(CollectionUtils.wrap(OAuth20Constants.SCOPE), context);
        if (map == null || map.isEmpty()) {
            return new ArrayList<>(0);
        }
        return (Collection<String>) map.get(OAuth20Constants.SCOPE);
    }