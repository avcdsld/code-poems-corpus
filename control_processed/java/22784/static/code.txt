public static RequestTemplate from(RequestTemplate requestTemplate) {
    RequestTemplate template =
        new RequestTemplate(requestTemplate.target, requestTemplate.fragment,
            requestTemplate.uriTemplate,
            requestTemplate.method, requestTemplate.charset,
            requestTemplate.body, requestTemplate.decodeSlash, requestTemplate.collectionFormat);

    if (!requestTemplate.queries().isEmpty()) {
      template.queries.putAll(requestTemplate.queries);
    }

    if (!requestTemplate.headers().isEmpty()) {
      template.headers.putAll(requestTemplate.headers);
    }
    return template;
  }