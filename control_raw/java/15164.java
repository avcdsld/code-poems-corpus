public CancellableContext withDeadlineAfter(long duration, TimeUnit unit,
                                              ScheduledExecutorService scheduler) {
    return withDeadline(Deadline.after(duration, unit), scheduler);
  }