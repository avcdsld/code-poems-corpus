public final Queue resumeQueue(String name) {

    ResumeQueueRequest request = ResumeQueueRequest.newBuilder().setName(name).build();
    return resumeQueue(request);
  }