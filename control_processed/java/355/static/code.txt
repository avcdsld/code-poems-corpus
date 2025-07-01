public RestTemplateBuilder interceptors(
			Collection<ClientHttpRequestInterceptor> interceptors) {
		Assert.notNull(interceptors, "interceptors must not be null");
		return new RestTemplateBuilder(this.detectRequestFactory, this.rootUri,
				this.messageConverters, this.requestFactorySupplier,
				this.uriTemplateHandler, this.errorHandler, this.basicAuthentication,
				this.restTemplateCustomizers, this.requestFactoryCustomizer,
				Collections.unmodifiableSet(new LinkedHashSet<>(interceptors)));
	}