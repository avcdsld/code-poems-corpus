public void fill3_1(byte[] bits, ByteBufferWrapper ab) {
      int bitoff = ab.get2();
      int nbytes = ab.get2();
      fill_1(bits, ab.position(), nbytes<<3, bitoff);
      ab.skip(nbytes);  // Skip inline bitset
    }