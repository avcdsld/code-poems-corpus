@Override
  public Boolean getbit(final byte[] key, final long offset) {
    checkIsInMultiOrPipeline();
    client.getbit(key, offset);
    return client.getIntegerReply() == 1;
  }