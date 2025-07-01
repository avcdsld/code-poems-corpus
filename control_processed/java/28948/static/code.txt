public final ListTasksPagedResponse listTasks(QueueName parent) {
    ListTasksRequest request =
        ListTasksRequest.newBuilder().setParent(parent == null ? null : parent.toString()).build();
    return listTasks(request);
  }