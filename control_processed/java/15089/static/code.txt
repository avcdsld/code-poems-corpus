private static <ReqT, RespT> ServerCallHandler<ReqT, RespT> asyncUnaryRequestCall(
      UnaryRequestMethod<ReqT, RespT> method) {
    return new UnaryServerCallHandler<>(method);
  }