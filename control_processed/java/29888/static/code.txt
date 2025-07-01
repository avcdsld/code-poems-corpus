static ImmutableList<ListAssetsResult> listAssetsWithQueryMarks(
      OrganizationName organizationName) {
    try (SecurityCenterClient client = SecurityCenterClient.create()) {
      // Start setting up a request for to list all assets filtered by a specific security mark.
      // OrganizationName organizationName = OrganizationName.of(/*organizationId=*/"123234324");
      ListAssetsRequest request =
          ListAssetsRequest.newBuilder()
              .setParent(organizationName.toString())
              .setFilter("security_marks.marks.key_a = \"value_a\"")
              .build();

      // Call the API.
      ListAssetsPagedResponse response = client.listAssets(request);

      // This creates one list for all assets.  If your organization has a large number of assets
      // this can cause out of memory issues.  You can process them batches by returning
      // the Iterable returned response.iterateAll() directly.
      ImmutableList<ListAssetsResult> results = ImmutableList.copyOf(response.iterateAll());
      System.out.println("Assets with security mark - key_a=value_a:");
      System.out.println(results);
      return results;
    } catch (IOException e) {
      throw new RuntimeException("Couldn't create client.", e);
    }
  }