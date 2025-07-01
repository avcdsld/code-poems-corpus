public OtpInputStream receiveBuf(final long timeout)
            throws InterruptedException, OtpErlangExit {
        final OtpMsg m = receiveMsg(timeout);
        if (m != null) {
            return m.getMsgBuf();
        }

        return null;
    }