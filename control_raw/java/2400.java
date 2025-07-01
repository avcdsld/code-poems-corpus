private ChunkFetchRequestHandler createChunkFetchHandler(TransportChannelHandler channelHandler,
      RpcHandler rpcHandler) {
    return new ChunkFetchRequestHandler(channelHandler.getClient(),
      rpcHandler.getStreamManager(), conf.maxChunksBeingTransferred());
  }