@Override
    public Object intercept(MethodInvocationContext<Object, Object> context) {
        AnnotationValue<Client> clientAnnotation = context.findAnnotation(Client.class).orElseThrow(() ->
                new IllegalStateException("Client advice called from type that is not annotated with @Client: " + context)
        );

        HttpClient httpClient = getClient(context, clientAnnotation);

        Class<?> declaringType = context.getDeclaringType();
        if (Closeable.class == declaringType || AutoCloseable.class == declaringType) {
            String clientId = clientAnnotation.getValue(String.class).orElse(null);
            String path = clientAnnotation.get("path", String.class).orElse(null);
            String clientKey = computeClientKey(clientId, path);
            clients.remove(clientKey);
            httpClient.close();
            return null;
        }

        Optional<Class<? extends Annotation>> httpMethodMapping = context.getAnnotationTypeByStereotype(HttpMethodMapping.class);
        if (context.hasStereotype(HttpMethodMapping.class) && httpClient != null) {
            AnnotationValue<HttpMethodMapping> mapping = context.getAnnotation(HttpMethodMapping.class);
            String uri = mapping.getRequiredValue(String.class);
            if (StringUtils.isEmpty(uri)) {
                uri = "/" + context.getMethodName();
            }

            Class<? extends Annotation> annotationType = httpMethodMapping.get();

            HttpMethod httpMethod = HttpMethod.valueOf(annotationType.getSimpleName().toUpperCase());

            ReturnType returnType = context.getReturnType();
            Class<?> javaReturnType = returnType.getType();

            UriMatchTemplate uriTemplate = UriMatchTemplate.of("");
            if (!(uri.length() == 1 && uri.charAt(0) == '/')) {
                uriTemplate = uriTemplate.nest(uri);
            }

            Map<String, Object> paramMap = context.getParameterValueMap();
            Map<String, String> queryParams = new LinkedHashMap<>();
            List<String> uriVariables = uriTemplate.getVariableNames();

            boolean variableSatisfied = uriVariables.isEmpty() || uriVariables.containsAll(paramMap.keySet());
            MutableHttpRequest<Object> request;
            Object body = null;
            Map<String, MutableArgumentValue<?>> parameters = context.getParameters();
            Argument[] arguments = context.getArguments();


            Map<String, String> headers = new LinkedHashMap<>(HEADERS_INITIAL_CAPACITY);

            List<AnnotationValue<Header>> headerAnnotations = context.getAnnotationValuesByType(Header.class);
            for (AnnotationValue<Header> headerAnnotation : headerAnnotations) {
                String headerName = headerAnnotation.get("name", String.class).orElse(null);
                String headerValue = headerAnnotation.getValue(String.class).orElse(null);
                if (StringUtils.isNotEmpty(headerName) && StringUtils.isNotEmpty(headerValue)) {
                    headers.put(headerName, headerValue);
                }
            }

            context.findAnnotation(Version.class)
                    .flatMap(versionAnnotation -> versionAnnotation.getValue(String.class))
                    .filter(StringUtils::isNotEmpty)
                    .ifPresent(version -> {

                        ClientVersioningConfiguration configuration = getVersioningConfiguration(clientAnnotation);

                        configuration.getHeaders()
                                .forEach(header -> headers.put(header, version));

                        configuration.getParameters()
                                .forEach(parameter -> queryParams.put(parameter, version));
                    });
          
            Map<String, Object> attributes = new LinkedHashMap<>(ATTRIBUTES_INITIAL_CAPACITY);

            List<AnnotationValue<RequestAttribute>> attributeAnnotations = context.getAnnotationValuesByType(RequestAttribute.class);
            for (AnnotationValue<RequestAttribute> attributeAnnotation : attributeAnnotations) {
                String attributeName = attributeAnnotation.get("name", String.class).orElse(null);
                Object attributeValue = attributeAnnotation.getValue(Object.class).orElse(null);
                if (StringUtils.isNotEmpty(attributeName) && attributeValue != null) {
                    attributes.put(attributeName, attributeValue);
                }
            }

            List<NettyCookie> cookies = new ArrayList<>();
            List<Argument> bodyArguments = new ArrayList<>();
            ConversionService<?> conversionService = ConversionService.SHARED;
            for (Argument argument : arguments) {
                String argumentName = argument.getName();
                AnnotationMetadata annotationMetadata = argument.getAnnotationMetadata();
                MutableArgumentValue<?> value = parameters.get(argumentName);
                Object definedValue = value.getValue();

                if (paramMap.containsKey(argumentName)) {
                    if (annotationMetadata.hasStereotype(Format.class)) {
                        final Object v = paramMap.get(argumentName);
                        if (v != null) {
                            paramMap.put(argumentName, conversionService.convert(v, ConversionContext.of(String.class).with(argument.getAnnotationMetadata())));
                        }
                    }
                }
                if (definedValue == null) {
                    definedValue = argument.getAnnotationMetadata().getValue(Bindable.class, "defaultValue", String.class).orElse(null);
                }

                if (definedValue == null && !argument.isAnnotationPresent(Nullable.class)) {
                    throw new IllegalArgumentException(
                            String.format("Null values are not allowed to be passed to client methods (%s). Add @javax.validation.Nullable if that is the desired behavior", context.getExecutableMethod().toString())
                    );
                }

                if (argument.isAnnotationPresent(Body.class)) {
                    body = definedValue;
                } else if (annotationMetadata.isAnnotationPresent(Header.class)) {

                    String headerName = annotationMetadata.getValue(Header.class, String.class).orElse(null);
                    if (StringUtils.isEmpty(headerName)) {
                        headerName = NameUtils.hyphenate(argumentName);
                    }
                    String finalHeaderName = headerName;
                    conversionService.convert(definedValue, String.class)
                        .ifPresent(o -> headers.put(finalHeaderName, o));
                } else if (annotationMetadata.isAnnotationPresent(CookieValue.class)) {
                    String cookieName = annotationMetadata.getValue(CookieValue.class, String.class).orElse(null);
                    if (StringUtils.isEmpty(cookieName)) {
                        cookieName = argumentName;
                    }
                    String finalCookieName = cookieName;

                    conversionService.convert(definedValue, String.class)
                        .ifPresent(o -> cookies.add(new NettyCookie(finalCookieName, o)));

                } else if (annotationMetadata.isAnnotationPresent(QueryValue.class)) {
                    String parameterName = annotationMetadata.getValue(QueryValue.class, String.class).orElse(null);
                    conversionService.convert(definedValue, ConversionContext.of(String.class).with(annotationMetadata)).ifPresent(o -> {
                        if (!StringUtils.isEmpty(parameterName)) {
                            paramMap.put(parameterName, o);
                            queryParams.put(parameterName, o);
                        } else {
                            queryParams.put(argumentName, o);
                        }
                    });
                } else if (annotationMetadata.isAnnotationPresent(RequestAttribute.class)) {
                    String attributeName = annotationMetadata.getValue(Annotation.class, String.class).orElse(null);
                    if (StringUtils.isEmpty(attributeName)) {
                        attributeName = NameUtils.hyphenate(argumentName);
                    }
                    String finalAttributeName = attributeName;
                    conversionService.convert(definedValue, Object.class)
                        .ifPresent(o -> attributes.put(finalAttributeName, o));
                } else if (annotationMetadata.isAnnotationPresent(PathVariable.class)) {
                    String parameterName = annotationMetadata.getValue(PathVariable.class, String.class).orElse(null);
                    conversionService.convert(definedValue, ConversionContext.of(String.class).with(annotationMetadata)).ifPresent(o -> {
                        if (!StringUtils.isEmpty(o)) {
                            paramMap.put(parameterName, o);
                        }
                    });
                } else if (!uriVariables.contains(argumentName)) {
                    bodyArguments.add(argument);
                }
            }

            if (HttpMethod.permitsRequestBody(httpMethod)) {
                if (body == null && !bodyArguments.isEmpty()) {
                    Map<String, Object> bodyMap = new LinkedHashMap<>();

                    for (Argument bodyArgument : bodyArguments) {
                        String argumentName = bodyArgument.getName();
                        MutableArgumentValue<?> value = parameters.get(argumentName);
                        bodyMap.put(argumentName, value.getValue());
                    }
                    body = bodyMap;
                }

                if (body != null) {
                    if (!variableSatisfied) {

                        if (body instanceof Map) {
                            paramMap.putAll((Map) body);
                        } else {
                            BeanMap<Object> beanMap = BeanMap.of(body);
                            for (Map.Entry<String, Object> entry : beanMap.entrySet()) {
                                String k = entry.getKey();
                                Object v = entry.getValue();
                                if (v != null) {
                                    paramMap.put(k, v);
                                }
                            }
                        }
                    }
                }
            }

            uri = uriTemplate.expand(paramMap);
            uriVariables.forEach(queryParams::remove);

            request = HttpRequest.create(httpMethod, appendQuery(uri, queryParams));
            if (body != null) {
                request.body(body);

                MediaType[] contentTypes = context.getValue(Produces.class, MediaType[].class).orElse(DEFAULT_ACCEPT_TYPES);
                if (ArrayUtils.isNotEmpty(contentTypes)) {
                    request.contentType(contentTypes[0]);
                }
            }

            // Set the URI template used to make the request for tracing purposes
            request.setAttribute(HttpAttributes.URI_TEMPLATE, resolveTemplate(clientAnnotation, uriTemplate.toString()));
            String serviceId = clientAnnotation.getValue(String.class).orElse(null);
            Argument<?> errorType = clientAnnotation.get("errorType", Class.class).map((Function<Class, Argument>) Argument::of).orElse(HttpClient.DEFAULT_ERROR_TYPE);
            request.setAttribute(HttpAttributes.SERVICE_ID, serviceId);


            if (!headers.isEmpty()) {
                for (Map.Entry<String, String> entry : headers.entrySet()) {
                    request.header(entry.getKey(), entry.getValue());
                }
            }

            cookies.forEach(request::cookie);

            if (!attributes.isEmpty()) {
                for (Map.Entry<String, Object> entry : attributes.entrySet()) {
                    request.setAttribute(entry.getKey(), entry.getValue());
                }
            }

            MediaType[] acceptTypes = context.getValue(Consumes.class, MediaType[].class).orElse(DEFAULT_ACCEPT_TYPES);

            boolean isFuture = CompletableFuture.class.isAssignableFrom(javaReturnType);
            final Class<?> methodDeclaringType = declaringType;
            if (Publishers.isConvertibleToPublisher(javaReturnType) || isFuture) {
                boolean isSingle = Publishers.isSingle(javaReturnType) || isFuture || context.getValue(Consumes.class, "single", Boolean.class).orElse(false);
                Argument<?> publisherArgument = returnType.asArgument().getFirstTypeVariable().orElse(Argument.OBJECT_ARGUMENT);


                Class<?> argumentType = publisherArgument.getType();

                if (HttpResponse.class.isAssignableFrom(argumentType) || HttpStatus.class.isAssignableFrom(argumentType)) {
                    isSingle = true;
                }

                Publisher<?> publisher;

                if (!isSingle && httpClient instanceof StreamingHttpClient) {
                    StreamingHttpClient streamingHttpClient = (StreamingHttpClient) httpClient;

                    if (!Void.class.isAssignableFrom(argumentType)) {
                        request.accept(acceptTypes);
                    }

                    if (HttpResponse.class.isAssignableFrom(argumentType) ||
                            Void.class.isAssignableFrom(argumentType)) {
                        publisher = streamingHttpClient.exchangeStream(
                                request
                        );
                    } else {
                        boolean isEventStream = Arrays.asList(acceptTypes).contains(MediaType.TEXT_EVENT_STREAM_TYPE);

                        if (isEventStream && streamingHttpClient instanceof SseClient) {
                            SseClient sseClient = (SseClient) streamingHttpClient;
                            if (publisherArgument.getType() == Event.class) {
                                publisher = sseClient.eventStream(
                                        request, publisherArgument.getFirstTypeVariable().orElse(Argument.OBJECT_ARGUMENT)
                                );
                            } else {
                                publisher = Flowable.fromPublisher(sseClient.eventStream(
                                        request, publisherArgument
                                )).map(Event::getData);
                            }
                        } else {
                            boolean isJson = isJsonParsedMediaType(acceptTypes);
                            if (isJson) {
                                publisher = streamingHttpClient.jsonStream(
                                        request, publisherArgument
                                );
                            } else {
                                Publisher<ByteBuffer<?>> byteBufferPublisher = streamingHttpClient.dataStream(
                                        request
                                );
                                if (argumentType == ByteBuffer.class) {
                                    publisher = byteBufferPublisher;
                                } else {
                                    if (conversionService.canConvert(ByteBuffer.class, argumentType)) {
                                        // It would be nice if we could capture the TypeConverter here
                                        publisher = Flowable.fromPublisher(byteBufferPublisher)
                                                .map(value -> conversionService.convert(value, argumentType).get());
                                    } else {
                                        throw new ConfigurationException("Cannot create the generated HTTP client's " +
                                                "required return type, since no TypeConverter from ByteBuffer to " +
                                                argumentType + " is registered");
                                    }
                                }

                            }
                        }
                    }

                } else {

                    if (Void.class.isAssignableFrom(argumentType)) {
                        publisher = httpClient.exchange(
                                request, null, errorType
                        );
                    } else {
                        request.accept(acceptTypes);
                        if (HttpResponse.class.isAssignableFrom(argumentType)) {
                            publisher = httpClient.exchange(
                                    request, publisherArgument, errorType
                            );
                        } else {
                            publisher = httpClient.retrieve(
                                    request, publisherArgument, errorType
                            );
                        }
                    }
                }

                if (isFuture) {
                    CompletableFuture<Object> future = new CompletableFuture<>();
                    publisher.subscribe(new CompletionAwareSubscriber<Object>() {
                        AtomicReference<Object> reference = new AtomicReference<>();

                        @Override
                        protected void doOnSubscribe(Subscription subscription) {
                            subscription.request(1);
                        }

                        @Override
                        protected void doOnNext(Object message) {
                            if (!Void.class.isAssignableFrom(argumentType)) {
                                reference.set(message);
                            }
                        }

                        @Override
                        protected void doOnError(Throwable t) {
                            if (t instanceof HttpClientResponseException) {
                                HttpClientResponseException e = (HttpClientResponseException) t;
                                if (e.getStatus() == HttpStatus.NOT_FOUND) {
                                    future.complete(null);
                                    return;
                                }
                            }
                            if (LOG.isErrorEnabled()) {
                                LOG.error("Client [" + methodDeclaringType.getName() + "] received HTTP error response: " + t.getMessage(), t);
                            }

                            future.completeExceptionally(t);
                        }

                        @Override
                        protected void doOnComplete() {
                            future.complete(reference.get());
                        }
                    });
                    return future;
                } else {
                    Object finalPublisher = conversionService.convert(publisher, javaReturnType).orElseThrow(() ->
                        new HttpClientException("Cannot convert response publisher to Reactive type (Unsupported Reactive type): " + javaReturnType)
                    );
                    for (ReactiveClientResultTransformer transformer : transformers) {
                        finalPublisher = transformer.transform(finalPublisher);
                    }
                    return finalPublisher;
                }
            } else {
                BlockingHttpClient blockingHttpClient = httpClient.toBlocking();

                if (void.class != javaReturnType) {
                    request.accept(acceptTypes);
                }

                if (HttpResponse.class.isAssignableFrom(javaReturnType)) {
                    return blockingHttpClient.exchange(
                        request, returnType.asArgument().getFirstTypeVariable().orElse(Argument.OBJECT_ARGUMENT), errorType
                    );
                } else if (void.class == javaReturnType) {
                    blockingHttpClient.exchange(request, null, errorType);
                    return null;
                } else {
                    try {
                        return blockingHttpClient.retrieve(
                                request, returnType.asArgument(), errorType
                        );
                    } catch (RuntimeException t) {
                        if (t instanceof HttpClientResponseException && ((HttpClientResponseException) t).getStatus() == HttpStatus.NOT_FOUND) {
                            if (javaReturnType == Optional.class) {
                                return Optional.empty();
                            }
                            return null;
                        } else {
                            throw t;
                        }
                    }
                }
            }
        }
        // try other introduction advice
        return context.proceed();
    }