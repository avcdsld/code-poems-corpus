private void recordSerializeResponse(RpcResponseCommand responseCommand) {
        if (!RpcInternalContext.isAttachmentEnable()) {
            return;
        }
        RpcInternalContext context = RpcInternalContext.getContext();
        int cost = context.getStopWatch().tick().read();
        int respSize = RpcProtocol.getResponseHeaderLength()
            + responseCommand.getClazzLength()
            + responseCommand.getContentLength()
            + responseCommand.getHeaderLength();
        // 记录响应序列化大小和请求序列化耗时
        context.setAttachment(RpcConstants.INTERNAL_KEY_RESP_SIZE, respSize);
        context.setAttachment(RpcConstants.INTERNAL_KEY_RESP_SERIALIZE_TIME, cost);
    }