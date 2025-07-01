public final ClientEvent createClientEvent(String parent, ClientEvent clientEvent) {

    CreateClientEventRequest request =
        CreateClientEventRequest.newBuilder().setParent(parent).setClientEvent(clientEvent).build();
    return createClientEvent(request);
  }