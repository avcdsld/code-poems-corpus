<RequestT, ResponseT> void streamRequest(
      RequestT requestT,
      ApiStreamObserver<ResponseT> responseObserverT,
      ServerStreamingCallable<RequestT, ResponseT> callable) {
    Preconditions.checkState(!closed, "Firestore client has already been closed");
    callable.serverStreamingCall(requestT, responseObserverT);
  }