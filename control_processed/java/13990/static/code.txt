public static HttpResponse execute(final String url,
                                       final String method,
                                       final String basicAuthUsername,
                                       final String basicAuthPassword,
                                       final Map<String, Object> parameters,
                                       final Map<String, Object> headers,
                                       final String entity) {
        try {
            val uri = buildHttpUri(url, parameters);
            val request = getHttpRequestByMethod(method.toLowerCase().trim(), entity, uri);
            headers.forEach((k, v) -> request.addHeader(k, v.toString()));
            prepareHttpRequest(request, basicAuthUsername, basicAuthPassword, parameters);
            return HTTP_CLIENT.execute(request);
        } catch (final Exception e) {
            LOGGER.error(e.getMessage(), e);
        }
        return null;
    }