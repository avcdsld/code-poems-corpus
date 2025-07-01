public short uShortValue() throws OtpErlangRangeException {
        final long l = longValue();
        final short i = (short) l;

        if (i != l) {
            throw new OtpErlangRangeException("Value too large for short: "
                    + val);
        } else if (i < 0) {
            throw new OtpErlangRangeException("Value not positive: " + val);
        }

        return i;
    }