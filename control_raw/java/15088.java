public static <ReqT, RespT> ServerCallHandler<ReqT, RespT> asyncBidiStreamingCall(
      BidiStreamingMethod<ReqT, RespT> method) {
    return asyncStreamingRequestCall(method);
  }