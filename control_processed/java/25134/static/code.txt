public static <T extends H2OCountedCompleter> T submitTask( T task ) {
    int priority = task.priority();
    if( priority < LOW_PRIORITY_API_WORK )
      LOW_PRIORITY_API_WORK_CLASS = task.getClass().toString();
    assert MIN_PRIORITY <= priority && priority <= MAX_PRIORITY:"priority " + priority + " is out of range, expected range is < " + MIN_PRIORITY + "," + MAX_PRIORITY + ">";
    if( FJPS[priority]==null )
      synchronized( H2O.class ) { if( FJPS[priority] == null ) FJPS[priority] = new PrioritizedForkJoinPool(priority,-1); }
    FJPS[priority].submit(task);
    return task;
  }