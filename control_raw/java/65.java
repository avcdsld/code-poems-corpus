public Object loadServiceCapabilities(String serviceUrl) throws IOException {
		HttpGet request = new HttpGet(serviceUrl);
		request.setHeader(
				new BasicHeader(HttpHeaders.ACCEPT, ACCEPT_SERVICE_CAPABILITIES));
		CloseableHttpResponse httpResponse = execute(request, serviceUrl,
				"retrieve help");
		validateResponse(httpResponse, serviceUrl);
		HttpEntity httpEntity = httpResponse.getEntity();
		ContentType contentType = ContentType.getOrDefault(httpEntity);
		if (contentType.getMimeType().equals("text/plain")) {
			return getContent(httpEntity);
		}
		return parseJsonMetadata(httpEntity);
	}