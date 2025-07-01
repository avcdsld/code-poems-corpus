private HandlerAdapter getHandlerAdapter(HttpRequest request) {
        for (HandlerAdapter ha : mAdapterList) {
            if (ha.intercept(request)) return ha;
        }
        return null;
    }