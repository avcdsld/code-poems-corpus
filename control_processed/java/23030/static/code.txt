protected void addSocketioHandlers(ChannelPipeline pipeline) {
        pipeline.addLast(HTTP_REQUEST_DECODER, new HttpRequestDecoder());
        pipeline.addLast(HTTP_AGGREGATOR, new HttpObjectAggregator(configuration.getMaxHttpContentLength()) {
            @Override
            protected Object newContinueResponse(HttpMessage start, int maxContentLength,
                    ChannelPipeline pipeline) {
                return null;
            }

        });
        pipeline.addLast(HTTP_ENCODER, new HttpResponseEncoder());

        if (configuration.isHttpCompression()) {
            pipeline.addLast(HTTP_COMPRESSION, new HttpContentCompressor());
        }

        pipeline.addLast(PACKET_HANDLER, packetHandler);

        pipeline.addLast(AUTHORIZE_HANDLER, authorizeHandler);
        pipeline.addLast(XHR_POLLING_TRANSPORT, xhrPollingTransport);
        // TODO use single instance when https://github.com/netty/netty/issues/4755 will be resolved
        if (configuration.isWebsocketCompression()) {
            pipeline.addLast(WEB_SOCKET_TRANSPORT_COMPRESSION, new WebSocketServerCompressionHandler());
        }
        pipeline.addLast(WEB_SOCKET_TRANSPORT, webSocketTransport);

        pipeline.addLast(SOCKETIO_ENCODER, encoderHandler);

        pipeline.addLast(WRONG_URL_HANDLER, wrongUrlHandler);
    }