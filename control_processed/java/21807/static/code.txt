@Singleton
    HttpServerHandler<HttpRequest<?>, HttpResponse<?>> httpServerHandler(HttpTracing httpTracing) {
        return HttpServerHandler.create(httpTracing, new HttpServerAdapter<HttpRequest<?>, HttpResponse<?>>() {
            @Override
            public String method(HttpRequest<?> request) {
                return request.getMethod().name();
            }

            @Override
            public String url(HttpRequest<?> request) {
                return request.getUri().toString();
            }

            @Override
            public String requestHeader(HttpRequest<?> request, String name) {
                return request.getHeaders().get(name);
            }

            @Override
            public Integer statusCode(HttpResponse<?> response) {
                return response.getStatus().getCode();
            }

            @Override
            public String route(HttpResponse<?> response) {
                Optional<String> value = response.getAttribute(HttpAttributes.URI_TEMPLATE, String.class);
                return value.orElseGet(() -> super.route(response));
            }

            @Override
            public String methodFromResponse(HttpResponse<?> httpResponse) {
                return httpResponse.getAttribute(HttpAttributes.METHOD_NAME, String.class).orElse(null);
            }

            @Override
            public boolean parseClientAddress(HttpRequest<?> httpRequest, Endpoint.Builder builder) {
                InetSocketAddress remoteAddress = httpRequest.getRemoteAddress();
                return builder.parseIp(remoteAddress.getAddress());
            }
        });
    }