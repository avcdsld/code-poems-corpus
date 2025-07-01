public static Http2Exception headerListSizeError(int id, Http2Error error, boolean onDecode,
            String fmt, Object... args) {
        return CONNECTION_STREAM_ID == id ?
                Http2Exception.connectionError(error, fmt, args) :
                    new HeaderListSizeException(id, error, String.format(fmt, args), onDecode);
    }