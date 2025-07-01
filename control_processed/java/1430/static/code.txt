public static void setKeepAlive(HttpMessage message, boolean keepAlive) {
        setKeepAlive(message.headers(), message.protocolVersion(), keepAlive);
    }