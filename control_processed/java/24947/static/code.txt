public short read_ushort() throws OtpErlangDecodeException {
        final long l = this.read_long(true);
        final short i = (short) l;

        if (l != (i & 0xffffL)) {
            throw new OtpErlangDecodeException("Value does not fit in ushort: "
                    + l);
        }

        return i;
    }