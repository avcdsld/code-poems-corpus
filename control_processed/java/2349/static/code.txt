@Override
    protected FullHttpRequest newHandshakeRequest() {
        // Get path
        URI wsURL = uri();
        String path = rawPath(wsURL);

        // Get 16 bit nonce and base 64 encode it
        byte[] nonce = WebSocketUtil.randomBytes(16);
        String key = WebSocketUtil.base64(nonce);

        String acceptSeed = key + MAGIC_GUID;
        byte[] sha1 = WebSocketUtil.sha1(acceptSeed.getBytes(CharsetUtil.US_ASCII));
        expectedChallengeResponseString = WebSocketUtil.base64(sha1);

        if (logger.isDebugEnabled()) {
            logger.debug(
                    "WebSocket version 08 client handshake key: {}, expected response: {}",
                    key, expectedChallengeResponseString);
        }

        // Format request
        FullHttpRequest request = new DefaultFullHttpRequest(HttpVersion.HTTP_1_1, HttpMethod.GET, path);
        HttpHeaders headers = request.headers();

        if (customHeaders != null) {
            headers.add(customHeaders);
        }

        headers.set(HttpHeaderNames.UPGRADE, HttpHeaderValues.WEBSOCKET)
               .set(HttpHeaderNames.CONNECTION, HttpHeaderValues.UPGRADE)
               .set(HttpHeaderNames.SEC_WEBSOCKET_KEY, key)
               .set(HttpHeaderNames.HOST, websocketHostValue(wsURL))
               .set(HttpHeaderNames.SEC_WEBSOCKET_ORIGIN, websocketOriginValue(wsURL));

        String expectedSubprotocol = expectedSubprotocol();
        if (expectedSubprotocol != null && !expectedSubprotocol.isEmpty()) {
            headers.set(HttpHeaderNames.SEC_WEBSOCKET_PROTOCOL, expectedSubprotocol);
        }

        headers.set(HttpHeaderNames.SEC_WEBSOCKET_VERSION, "8");
        return request;
    }