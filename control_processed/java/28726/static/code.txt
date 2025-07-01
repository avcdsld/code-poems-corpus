public final ListLogMetricsPagedResponse listLogMetrics(ParentName parent) {
    ListLogMetricsRequest request =
        ListLogMetricsRequest.newBuilder()
            .setParent(parent == null ? null : parent.toString())
            .build();
    return listLogMetrics(request);
  }