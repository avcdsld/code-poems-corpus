@Override
    public void close() {
        if (!this.closed.get()) {
            Futures.await(Services.stopAsync(this, this.executor));
            log.info("{}: Closed.", this.traceObjectId);
            this.closed.set(true);
        }
    }