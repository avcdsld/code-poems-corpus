private TimerTask getTimerTask() {
    final TimeBasedReportingMetric<T> lockObject = this;
    final TimerTask recurringReporting = new TimerTask() {
      @Override
      public void run() {
        synchronized (lockObject) {
          preTrackingEventMethod();
          notifyManager();
          postTrackingEventMethod();
        }
      }
    };
    return recurringReporting;
  }