@Override
    public Observable<HttpClientResponse<O>> submit(HttpClientRequest<I> request) {
        return submit(request, null, null);
    }