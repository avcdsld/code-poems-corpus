public final ListMetricDescriptorsPagedResponse listMetricDescriptors(String name) {
    ListMetricDescriptorsRequest request =
        ListMetricDescriptorsRequest.newBuilder().setName(name).build();
    return listMetricDescriptors(request);
  }