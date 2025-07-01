private void checkExecuteConditions(HttpState state, HttpConnection conn)
    throws HttpException {

        if (state == null) {
            throw new IllegalArgumentException("HttpState parameter may not be null");
        }
        if (conn == null) {
            throw new IllegalArgumentException("HttpConnection parameter may not be null");
        }
        if (this.aborted) {
            throw new IllegalStateException("Method has been aborted");
        }
        if (!validate()) {
            throw new ProtocolException("HttpMethodBase object not valid");
        }
    }