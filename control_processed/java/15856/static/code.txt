private void removeWorker(final Worker worker)
  {
    log.info("Kaboom! Worker[%s] removed!", worker.getHost());

    final ZkWorker zkWorker = zkWorkers.get(worker.getHost());
    if (zkWorker != null) {
      try {
        scheduleTasksCleanupForWorker(worker.getHost(), getAssignedTasks(worker));
      }
      catch (Exception e) {
        throw new RuntimeException(e);
      }
      finally {
        try {
          zkWorker.close();
        }
        catch (Exception e) {
          log.error(e, "Exception closing worker[%s]!", worker.getHost());
        }
        zkWorkers.remove(worker.getHost());
        checkBlackListedNodes();
      }
    }
    lazyWorkers.remove(worker.getHost());
  }