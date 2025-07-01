@Override
  public int write(ByteBuffer src) {
    int toTransfer = Math.min(src.remaining(), data.length - offset);
    src.get(data, offset, toTransfer);
    offset += toTransfer;
    return toTransfer;
  }