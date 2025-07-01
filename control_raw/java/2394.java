@Override
  public void userEventTriggered(ChannelHandlerContext ctx, Object evt) throws Exception {
    if (evt instanceof IdleStateEvent) {
      IdleStateEvent e = (IdleStateEvent) evt;
      // See class comment for timeout semantics. In addition to ensuring we only timeout while
      // there are outstanding requests, we also do a secondary consistency check to ensure
      // there's no race between the idle timeout and incrementing the numOutstandingRequests
      // (see SPARK-7003).
      //
      // To avoid a race between TransportClientFactory.createClient() and this code which could
      // result in an inactive client being returned, this needs to run in a synchronized block.
      synchronized (this) {
        boolean hasInFlightRequests = responseHandler.numOutstandingRequests() > 0;
        boolean isActuallyOverdue =
          System.nanoTime() - responseHandler.getTimeOfLastRequestNs() > requestTimeoutNs;
        if (e.state() == IdleState.ALL_IDLE && isActuallyOverdue) {
          if (hasInFlightRequests) {
            String address = getRemoteAddress(ctx.channel());
            logger.error("Connection to {} has been quiet for {} ms while there are outstanding " +
              "requests. Assuming connection is dead; please adjust spark.network.timeout if " +
              "this is wrong.", address, requestTimeoutNs / 1000 / 1000);
            client.timeOut();
            ctx.close();
          } else if (closeIdleConnections) {
            // While CloseIdleConnections is enable, we also close idle connection
            client.timeOut();
            ctx.close();
          }
        }
      }
    }
    ctx.fireUserEventTriggered(evt);
  }