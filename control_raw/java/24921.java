protected void sendLink(final OtpErlangPid from, final OtpErlangPid dest)
            throws IOException {
        if (!connected) {
            throw new IOException("Not connected");
        }
        @SuppressWarnings("resource")
        final OtpOutputStream header = new OtpOutputStream(headerLen);

        // preamble: 4 byte length + "passthrough" tag
        header.write4BE(0); // reserve space for length
        header.write1(passThrough);
        header.write1(version);

        // header
        header.write_tuple_head(3);
        header.write_long(linkTag);
        header.write_any(from);
        header.write_any(dest);

        // fix up length in preamble
        header.poke4BE(0, header.size() - 4);

        do_send(header);
    }