@SuppressWarnings("unchecked")
    public <T> T readInbound() {
        T message = (T) poll(inboundMessages);
        if (message != null) {
            ReferenceCountUtil.touch(message, "Caller of readInbound() will handle the message from this point");
        }
        return message;
    }