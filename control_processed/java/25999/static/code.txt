@Override
  public List<byte[]> lrange(final byte[] key, final long start, final long stop) {
    checkIsInMultiOrPipeline();
    client.lrange(key, start, stop);
    return client.getBinaryMultiBulkReply();
  }