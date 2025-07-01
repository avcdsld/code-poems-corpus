public final SplitReadStreamResponse splitReadStream(Stream originalStream) {
    SplitReadStreamRequest request =
        SplitReadStreamRequest.newBuilder().setOriginalStream(originalStream).build();
    return splitReadStream(request);
  }