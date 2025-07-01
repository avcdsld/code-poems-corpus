public static HttpResponse executePost(final String url,
                                           final String entity,
                                           final Map<String, Object> parameters) {
        return executePost(url, null, null, entity, parameters);
    }