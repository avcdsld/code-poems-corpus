public ProjectGenerationResponse generate(ProjectGenerationRequest request)
			throws IOException {
		Log.info("Using service at " + request.getServiceUrl());
		InitializrServiceMetadata metadata = loadMetadata(request.getServiceUrl());
		URI url = request.generateUrl(metadata);
		CloseableHttpResponse httpResponse = executeProjectGenerationRequest(url);
		HttpEntity httpEntity = httpResponse.getEntity();
		validateResponse(httpResponse, request.getServiceUrl());
		return createResponse(httpResponse, httpEntity);
	}