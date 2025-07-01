@Nullable
  public static com.google.rpc.Status fromStatusAndTrailers(Status status, Metadata trailers) {
    if (trailers != null) {
      com.google.rpc.Status statusProto = trailers.get(STATUS_DETAILS_KEY);
      if (statusProto != null) {
        checkArgument(
            status.getCode().value() == statusProto.getCode(),
            "com.google.rpc.Status code must match gRPC status code");
        return statusProto;
      }
    }
    return null;
  }