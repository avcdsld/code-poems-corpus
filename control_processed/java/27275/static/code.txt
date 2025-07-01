public CompletableFuture<Void> initialize(Duration timeout) {
        if (isInitialized()) {
            log.warn("Reinitializing.");
        }

        TimeoutTimer timer = new TimeoutTimer(timeout);
        return this.getLength
                .apply(timer.getRemaining())
                .thenCompose(length -> {
                    if (length <= FOOTER_LENGTH) {
                        // Empty index.
                        setState(length, PagePointer.NO_OFFSET, 0);
                        return CompletableFuture.completedFuture(null);
                    }

                    long footerOffset = getFooterOffset(length);
                    return this.read
                            .apply(footerOffset, FOOTER_LENGTH, timer.getRemaining())
                            .thenAccept(footer -> initialize(footer, footerOffset, length));
                });
    }