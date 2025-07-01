public Object fromBytes(byte[] data, int start, int numBytes)
  {
    ByteBuffer bb = ByteBuffer.wrap(data);
    if (start > 0) {
      bb.position(start);
    }
    return getObjectStrategy().fromByteBuffer(bb, numBytes);
  }