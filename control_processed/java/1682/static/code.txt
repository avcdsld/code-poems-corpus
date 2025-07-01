public Future<Channel> renegotiate() {
        ChannelHandlerContext ctx = this.ctx;
        if (ctx == null) {
            throw new IllegalStateException();
        }

        return renegotiate(ctx.executor().<Channel>newPromise());
    }