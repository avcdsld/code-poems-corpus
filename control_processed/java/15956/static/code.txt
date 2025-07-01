protected ZuulFilter<HttpRequestMessage, HttpResponseMessage> newProxyEndpoint(HttpRequestMessage zuulRequest) {
        return new ProxyEndpoint(zuulRequest, getChannelHandlerContext(zuulRequest), getNextStage(), MethodBinding.NO_OP_BINDING);
    }