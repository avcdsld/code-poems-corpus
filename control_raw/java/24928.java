protected int readSock(final OtpTransport s, final byte[] b)
            throws IOException {
        int got = 0;
        final int len = b.length;
        int i;

        synchronized (this) {
            if (s == null) {
                throw new IOException("expected " + len
                        + " bytes, socket was closed");
            }
        }

        while (got < len) {
            i = s.getInputStream().read(b, got, len - got);

            if (i < 0) {
                throw new IOException("expected " + len
                        + " bytes, got EOF after " + got + " bytes");
            } else if (i == 0 && len != 0) {
                /*
                 * This is a corner case. According to
                 * http://java.sun.com/j2se/1.4.2/docs/api/ class InputStream
                 * is.read(,,l) can only return 0 if l==0. In other words it
                 * should not happen, but apparently did.
                 */
                throw new IOException("Remote connection closed");
            } else {
                got += i;
            }
        }
        return got;
    }