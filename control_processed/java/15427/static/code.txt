private static JsonParserIterator<TaskStatusPlus> getTasks(
      DruidLeaderClient indexingServiceClient,
      ObjectMapper jsonMapper,
      BytesAccumulatingResponseHandler responseHandler
  )
  {
    Request request;
    try {
      request = indexingServiceClient.makeRequest(
          HttpMethod.GET,
          StringUtils.format("/druid/indexer/v1/tasks"),
          false
      );
    }
    catch (IOException e) {
      throw new RuntimeException(e);
    }
    ListenableFuture<InputStream> future = indexingServiceClient.goAsync(
        request,
        responseHandler
    );

    final JavaType typeRef = jsonMapper.getTypeFactory().constructType(new TypeReference<TaskStatusPlus>()
    {
    });
    return new JsonParserIterator<>(
        typeRef,
        future,
        request.getUrl().toString(),
        null,
        request.getUrl().getHost(),
        jsonMapper,
        responseHandler
    );
  }