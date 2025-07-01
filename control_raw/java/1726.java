@Override
    public void channelHandlerContext(ChannelHandlerContext ctx) throws Http2Exception {
        this.ctx = checkNotNull(ctx, "ctx");

        // Writing the pending bytes will not check writability change and instead a writability change notification
        // to be provided by an explicit call.
        channelWritabilityChanged();

        // Don't worry about cleaning up queued frames here if ctx is null. It is expected that all streams will be
        // closed and the queue cleanup will occur when the stream state transitions occur.

        // If any frames have been queued up, we should send them now that we have a channel context.
        if (isChannelWritable()) {
            writePendingBytes();
        }
    }