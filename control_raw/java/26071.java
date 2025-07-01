@Service
    public Task poll(String taskType, String workerId, String domain) {
        LOGGER.debug("Task being polled: /tasks/poll/{}?{}&{}", taskType, workerId, domain);
        Task task = executionService.getLastPollTask(taskType, workerId, domain);
        if (task != null) {
            LOGGER.debug("The Task {} being returned for /tasks/poll/{}?{}&{}", task, taskType, workerId, domain);
        }
        Monitors.recordTaskPollCount(taskType, domain, 1);
        return task;
    }