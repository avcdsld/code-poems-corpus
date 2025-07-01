@Override
    @SneakyThrows(Exception.class)
    public void close() {
        ReusableLatch waitSignal = null;
        synchronized (this.stateLock) {
            if (this.closed) {
                return;
            }

            this.closed = true;
            if (this.activeCount != 0 || !this.pendingItems.isEmpty()) {
                // Setup a latch that will be released when the last item completes.
                this.emptyNotifier = new ReusableLatch(false);
                waitSignal = this.emptyNotifier;
            }
        }

        if (waitSignal != null) {
            // We have unfinished items. Wait for them.
            waitSignal.await(CLOSE_TIMEOUT_MILLIS);
        }
    }