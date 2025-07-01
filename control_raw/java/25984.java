@Override
  public Long append(final byte[] key, final byte[] value) {
    checkIsInMultiOrPipeline();
    client.append(key, value);
    return client.getIntegerReply();
  }