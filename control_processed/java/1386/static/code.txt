static InetAddress decodeAddress(DnsRecord record, String name, boolean decodeIdn) {
        if (!(record instanceof DnsRawRecord)) {
            return null;
        }
        final ByteBuf content = ((ByteBufHolder) record).content();
        final int contentLen = content.readableBytes();
        if (contentLen != INADDRSZ4 && contentLen != INADDRSZ6) {
            return null;
        }

        final byte[] addrBytes = new byte[contentLen];
        content.getBytes(content.readerIndex(), addrBytes);

        try {
            return InetAddress.getByAddress(decodeIdn ? IDN.toUnicode(name) : name, addrBytes);
        } catch (UnknownHostException e) {
            // Should never reach here.
            throw new Error(e);
        }
    }