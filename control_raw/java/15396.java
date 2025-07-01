public static void scheduleAtFixedRate(
      final ScheduledExecutorService exec,
      final Duration initialDelay,
      final Duration period,
      final Runnable runnable
  )
  {
    scheduleAtFixedRate(exec, initialDelay, period, new Callable<Signal>()
    {
      @Override
      public Signal call()
      {
        runnable.run();
        return Signal.REPEAT;
      }
    });
  }