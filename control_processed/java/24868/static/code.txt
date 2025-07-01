public void write8LE(final long n) {
        write((byte) (n & 0xff));
        write((byte) (n >> 8 & 0xff));
        write((byte) (n >> 16 & 0xff));
        write((byte) (n >> 24 & 0xff));
        write((byte) (n >> 32 & 0xff));
        write((byte) (n >> 40 & 0xff));
        write((byte) (n >> 48 & 0xff));
        write((byte) (n >> 56 & 0xff));
    }