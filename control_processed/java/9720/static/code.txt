@Override
    public V poll(long timeout, TimeUnit unit) throws InterruptedException {
        return get(pollAsync(timeout, unit));
    }