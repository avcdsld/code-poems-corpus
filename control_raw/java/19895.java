protected void addProxyConnectionHeader(HttpState state,
                                            HttpConnection conn)
    throws IOException, HttpException {
        LOG.trace("enter HttpMethodBase.addProxyConnectionHeader("
                  + "HttpState, HttpConnection)");
        if (!conn.isTransparent()) {
        	if (getRequestHeader("Proxy-Connection") == null) {
                addRequestHeader("Proxy-Connection", "Keep-Alive");
        	}
        }
    }