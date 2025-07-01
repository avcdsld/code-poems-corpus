public static Channel interceptForward(Channel channel,
                                         List<? extends ClientInterceptor> interceptors) {
    List<? extends ClientInterceptor> copy = new ArrayList<>(interceptors);
    Collections.reverse(copy);
    return intercept(channel, copy);
  }