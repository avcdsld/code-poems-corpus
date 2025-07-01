public void releaseExceptionallyAndReset(Throwable e) {
        ArrayList<CompletableFuture<T>> toComplete = null;
        synchronized (lock) {
            if (!waitingFutures.isEmpty()) {
                toComplete = new ArrayList<>(waitingFutures);
                waitingFutures.clear();
            }
            released = false;
            this.e = null;
            result = null;
            runningThreadId = null;
        }
        if (toComplete != null) {
            for (CompletableFuture<T> f : toComplete) {
                f.completeExceptionally(e);
            }
        }
    }