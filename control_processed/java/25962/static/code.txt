@Override
  public Long unlink(final byte[]... keys) {
    checkIsInMultiOrPipeline();
    client.unlink(keys);
    return client.getIntegerReply();
  }