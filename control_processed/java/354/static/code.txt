public RestTemplateBuilder interceptors(
			ClientHttpRequestInterceptor... interceptors) {
		Assert.notNull(interceptors, "interceptors must not be null");
		return interceptors(Arrays.asList(interceptors));
	}