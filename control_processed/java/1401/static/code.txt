public ChannelFlushPromiseNotifier notifyPromises(Throwable cause) {
        notifyPromises();
        for (;;) {
            FlushCheckpoint cp = flushCheckpoints.poll();
            if (cp == null) {
                break;
            }
            if (tryNotify) {
                cp.promise().tryFailure(cause);
            } else {
                cp.promise().setFailure(cause);
            }
        }
        return this;
    }