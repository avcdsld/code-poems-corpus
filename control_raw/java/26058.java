public List<TaskExecLog> getTaskLogs(String taskId) {
        Preconditions.checkArgument(StringUtils.isNotBlank(taskId), "Task id cannot be blank");
        return getForEntity("tasks/{taskId}/log", null, taskExecLogList, taskId);
    }