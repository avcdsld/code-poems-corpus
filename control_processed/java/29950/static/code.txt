public final void deleteAppProfile(AppProfileName name) {

    DeleteAppProfileRequest request =
        DeleteAppProfileRequest.newBuilder().setName(name == null ? null : name.toString()).build();
    deleteAppProfile(request);
  }