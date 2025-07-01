public final void deleteTenant(String name) {

    DeleteTenantRequest request = DeleteTenantRequest.newBuilder().setName(name).build();
    deleteTenant(request);
  }