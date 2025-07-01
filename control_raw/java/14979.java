void cancel(boolean permanent) {
    enabled = false;
    if (permanent && wakeUp != null) {
      wakeUp.cancel(false);
      wakeUp = null;
    }
  }