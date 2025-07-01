public final Tenant updateTenant(Tenant tenant) {

    UpdateTenantRequest request = UpdateTenantRequest.newBuilder().setTenant(tenant).build();
    return updateTenant(request);
  }