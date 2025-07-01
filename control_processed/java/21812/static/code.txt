private void removeHandlerIfActive(ChannelHandlerContext ctx, String name) {
        if (ctx.channel().isActive()) {
            ChannelPipeline pipeline = ctx.pipeline();
            ChannelHandler handler = pipeline.get(name);
            if (handler != null) {
                pipeline.remove(name);
            }
        }
    }