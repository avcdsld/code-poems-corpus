public static HttpResponse executePost(final String url,
                                           final String basicAuthUsername,
                                           final String basicAuthPassword,
                                           final String entity,
                                           final Map<String, Object> parameters,
                                           final Map<String, Object> headers) {
        try {
            return execute(url, HttpMethod.POST.name(), basicAuthUsername, basicAuthPassword, parameters, headers, entity);
        } catch (final Exception e) {
            LOGGER.error(e.getMessage(), e);
        }
        return null;
    }