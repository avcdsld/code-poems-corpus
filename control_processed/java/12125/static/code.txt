private Lease lease(@Nonnull FilePath p) {
        return new Lease(p) {
            final AtomicBoolean released = new AtomicBoolean();
            public void release() {
                _release(path);
            }
            @Override public void close() {
                if (released.compareAndSet(false, true)) {
                    release();
                }
            }
        };
    }