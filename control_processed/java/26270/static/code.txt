public Task getTaskDetails(String taskId) {
        Preconditions.checkArgument(StringUtils.isNotBlank(taskId), "Task id cannot be blank");
        return protoMapper.fromProto(
                stub.getTask(TaskServicePb.GetTaskRequest.newBuilder()
                        .setTaskId(taskId)
                        .build()
                ).getTask()
        );
    }