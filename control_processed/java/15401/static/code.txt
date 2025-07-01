public boolean add(final Task task) throws EntryExistsException
  {
    if (taskStorage.getTask(task.getId()).isPresent()) {
      throw new EntryExistsException(StringUtils.format("Task %s is already exists", task.getId()));
    }

    giant.lock();

    try {
      Preconditions.checkState(active, "Queue is not active!");
      Preconditions.checkNotNull(task, "task");
      Preconditions.checkState(tasks.size() < config.getMaxSize(), "Too many tasks (max = %,d)", config.getMaxSize());

      // If this throws with any sort of exception, including TaskExistsException, we don't want to
      // insert the task into our queue. So don't catch it.
      taskStorage.insert(task, TaskStatus.running(task.getId()));
      addTaskInternal(task);
      managementMayBeNecessary.signalAll();
      return true;
    }
    finally {
      giant.unlock();
    }
  }