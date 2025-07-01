@Override
  public void shutdown(final String taskId, String reason)
  {
    log.info("Shutdown [%s] because: [%s]", taskId, reason);
    if (!lifecycleLock.awaitStarted(1, TimeUnit.SECONDS)) {
      log.info("This TaskRunner is stopped or not yet started. Ignoring shutdown command for task: %s", taskId);
    } else if (pendingTasks.remove(taskId) != null) {
      pendingTaskPayloads.remove(taskId);
      log.info("Removed task from pending queue: %s", taskId);
    } else if (completeTasks.containsKey(taskId)) {
      cleanup(taskId);
    } else {
      final ZkWorker zkWorker = findWorkerRunningTask(taskId);

      if (zkWorker == null) {
        log.info("Can't shutdown! No worker running task %s", taskId);
        return;
      }
      URL url = null;
      try {
        url = TaskRunnerUtils.makeWorkerURL(zkWorker.getWorker(), "/druid/worker/v1/task/%s/shutdown", taskId);
        final StatusResponseHolder response = httpClient.go(
            new Request(HttpMethod.POST, url),
            RESPONSE_HANDLER,
            shutdownTimeout
        ).get();

        log.info(
            "Sent shutdown message to worker: %s, status %s, response: %s",
            zkWorker.getWorker().getHost(),
            response.getStatus(),
            response.getContent()
        );

        if (!HttpResponseStatus.OK.equals(response.getStatus())) {
          log.error("Shutdown failed for %s! Are you sure the task was running?", taskId);
        }
      }
      catch (InterruptedException e) {
        Thread.currentThread().interrupt();
        throw new RE(e, "Interrupted posting shutdown to [%s] for task [%s]", url, taskId);
      }
      catch (Exception e) {
        throw new RE(e, "Error in handling post to [%s] for task [%s]", zkWorker.getWorker().getHost(), taskId);
      }
    }
  }