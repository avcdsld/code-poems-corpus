private static void insertAddressUsingCallable(AddressClient client, String newAddressName)
      throws InterruptedException, ExecutionException {
    // Begin samplegen code for insertAddress().
    ProjectRegionName region = ProjectRegionName.of(PROJECT_NAME, REGION);
    Address address = Address.newBuilder().build();
    InsertAddressHttpRequest request =
        InsertAddressHttpRequest.newBuilder()
            .setRegion(region.toString())
            .setAddressResource(address)
            .build();
    ApiFuture<Operation> future = client.insertAddressCallable().futureCall(request);
    // Do something
    Operation response = future.get();

    // End samplegen code for insertAddress().
    System.out.format("Result of insert: %s\n", response.toString());
  }