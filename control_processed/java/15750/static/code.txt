@Nullable
  private TaskLockPosse createOrFindLockPosse(
      final Task task,
      final Interval interval,
      @Nullable final String preferredVersion,
      final TaskLockType lockType
  )
  {
    giant.lock();

    try {
      return createOrFindLockPosse(
          lockType,
          task.getId(),
          task.getGroupId(),
          task.getDataSource(),
          interval,
          preferredVersion,
          task.getPriority(),
          false
      );
    }
    finally {
      giant.unlock();
    }
  }