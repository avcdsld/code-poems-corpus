static PemEncoded toPEM(ByteBufAllocator allocator, boolean useDirect, PrivateKey key) {
        // We can take a shortcut if the private key happens to be already
        // PEM/PKCS#8 encoded. This is the ideal case and reason why all
        // this exists. It allows the user to pass pre-encoded bytes straight
        // into OpenSSL without having to do any of the extra work.
        if (key instanceof PemEncoded) {
            return ((PemEncoded) key).retain();
        }

        byte[] bytes = key.getEncoded();
        if (bytes == null) {
            throw new IllegalArgumentException(key.getClass().getName() + " does not support encoding");
        }

        return toPEM(allocator, useDirect, bytes);
    }