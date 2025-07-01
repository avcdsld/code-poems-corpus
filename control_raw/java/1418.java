@Override
    public void onError(ChannelHandlerContext ctx, boolean outbound, Throwable cause) {
        Http2Exception embedded = getEmbeddedHttp2Exception(cause);
        if (isStreamError(embedded)) {
            onStreamError(ctx, outbound, cause, (StreamException) embedded);
        } else if (embedded instanceof CompositeStreamException) {
            CompositeStreamException compositException = (CompositeStreamException) embedded;
            for (StreamException streamException : compositException) {
                onStreamError(ctx, outbound, cause, streamException);
            }
        } else {
            onConnectionError(ctx, outbound, cause, embedded);
        }
        ctx.flush();
    }