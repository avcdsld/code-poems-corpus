@Override
  public final void shutdownNow(Status status) {
    shutdown(status);
    Collection<PendingStream> savedPendingStreams;
    Runnable savedReportTransportTerminated;
    synchronized (lock) {
      savedPendingStreams = pendingStreams;
      savedReportTransportTerminated = reportTransportTerminated;
      reportTransportTerminated = null;
      if (!pendingStreams.isEmpty()) {
        pendingStreams = Collections.emptyList();
      }
    }
    if (savedReportTransportTerminated != null) {
      for (PendingStream stream : savedPendingStreams) {
        stream.cancel(status);
      }
      syncContext.execute(savedReportTransportTerminated);
    }
    // If savedReportTransportTerminated == null, transportTerminated() has already been called in
    // shutdown().
  }