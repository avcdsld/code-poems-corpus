private static void onDataRead(ChannelHandlerContext ctx, Http2DataFrame data) throws Exception {
        Http2FrameStream stream = data.stream();

        if (data.isEndStream()) {
            sendResponse(ctx, stream, data.content());
        } else {
            // We do not send back the response to the remote-peer, so we need to release it.
            data.release();
        }

        // Update the flowcontroller
        ctx.write(new DefaultHttp2WindowUpdateFrame(data.initialFlowControlledBytes()).stream(stream));
    }