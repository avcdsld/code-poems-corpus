public final Task cancelLease(String name, Timestamp scheduleTime) {

    CancelLeaseRequest request =
        CancelLeaseRequest.newBuilder().setName(name).setScheduleTime(scheduleTime).build();
    return cancelLease(request);
  }