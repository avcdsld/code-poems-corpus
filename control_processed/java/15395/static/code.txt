public static void scheduleWithFixedDelay(ScheduledExecutorService exec, Duration delay, Callable<Signal> callable)
  {
    scheduleWithFixedDelay(exec, delay, delay, callable);
  }