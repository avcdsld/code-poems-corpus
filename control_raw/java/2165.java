public final ChannelFuture spliceTo(final AbstractEpollStreamChannel ch, final int len,
                                        final ChannelPromise promise) {
        if (ch.eventLoop() != eventLoop()) {
            throw new IllegalArgumentException("EventLoops are not the same.");
        }
        checkPositiveOrZero(len, "len");
        if (ch.config().getEpollMode() != EpollMode.LEVEL_TRIGGERED
                || config().getEpollMode() != EpollMode.LEVEL_TRIGGERED) {
            throw new IllegalStateException("spliceTo() supported only when using " + EpollMode.LEVEL_TRIGGERED);
        }
        checkNotNull(promise, "promise");
        if (!isOpen()) {
            promise.tryFailure(SPLICE_TO_CLOSED_CHANNEL_EXCEPTION);
        } else {
            addToSpliceQueue(new SpliceInChannelTask(ch, len, promise));
            failSpliceIfClosed(promise);
        }
        return promise;
    }