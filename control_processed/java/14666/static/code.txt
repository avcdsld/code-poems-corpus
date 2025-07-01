public NettyServerBuilder workerEventLoopGroup(EventLoopGroup group) {
    if (group != null) {
      return workerEventLoopGroupPool(new FixedObjectPool<>(group));
    }
    return workerEventLoopGroupPool(DEFAULT_WORKER_EVENT_LOOP_GROUP_POOL);
  }