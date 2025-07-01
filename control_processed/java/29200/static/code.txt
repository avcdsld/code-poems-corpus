<RequestT, ResponseT> ApiFuture<ResponseT> sendRequest(
      RequestT requestT, UnaryCallable<RequestT, ResponseT> callable) {
    Preconditions.checkState(!closed, "Firestore client has already been closed");
    return callable.futureCall(requestT);
  }