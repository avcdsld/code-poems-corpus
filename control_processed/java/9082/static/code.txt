@Override
    public void dumpResponse(Map<String, Object> result) {
        byte[] responseBodyAttachment = exchange.getAttachment(StoreResponseStreamSinkConduit.RESPONSE);
        if(responseBodyAttachment != null) {
            this.bodyContent = config.isMaskEnabled() ? Mask.maskJson(new ByteArrayInputStream(responseBodyAttachment), "responseBody") : new String(responseBodyAttachment, UTF_8);
        }
        this.putDumpInfoTo(result);
    }