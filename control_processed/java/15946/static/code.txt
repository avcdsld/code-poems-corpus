protected void gracefullyWithDelay(ChannelHandlerContext ctx, Channel channel, ChannelPromise promise)
    {
        // See javadoc for explanation of why this may be disabled.
        if (! ALLOW_GRACEFUL_DELAYED.get()) {
            gracefully(channel, promise);
            return;
        }

        if (isAlreadyClosing(channel)) {
            promise.setSuccess();
            return;
        }

        // First send a 'graceful shutdown' GOAWAY frame.
        /*
        "A server that is attempting to gracefully shut down a connection SHOULD send an initial GOAWAY frame with
        the last stream identifier set to 231-1 and a NO_ERROR code. This signals to the client that a shutdown is
        imminent and that initiating further requests is prohibited."
          -- https://http2.github.io/http2-spec/#GOAWAY
         */
        DefaultHttp2GoAwayFrame goaway = new DefaultHttp2GoAwayFrame(Http2Error.NO_ERROR);
        goaway.setExtraStreamIds(Integer.MAX_VALUE);
        channel.writeAndFlush(goaway);
        LOG.debug("gracefullyWithDelay: flushed initial go_away frame. channel=" + channel.id().asShortText());

        // In N secs time, throw an error that causes the http2 codec to send another GOAWAY frame
        // (this time with accurate lastStreamId) and then close the connection.
        ctx.executor().schedule(() -> {

            // Check that the client hasn't already closed the connection (due to the earlier goaway we sent).
            gracefulConnectionShutdown(channel);
            promise.setSuccess();

        }, gracefulCloseDelay, TimeUnit.SECONDS);
    }