public List<Acl> updateDatasetAccess(DatasetInfo dataset) {
    // [START bigquery_update_dataset_access]
    List<Acl> beforeAcls = dataset.getAcl();

    // Make a copy of the ACLs so that they can be modified.
    ArrayList<Acl> acls = new ArrayList<>(beforeAcls);
    acls.add(Acl.of(new Acl.User("sample.bigquery.dev@gmail.com"), Acl.Role.READER));
    DatasetInfo.Builder builder = dataset.toBuilder();
    builder.setAcl(acls);

    bigquery.update(builder.build()); // API request.
    // [END bigquery_update_dataset_access]

    return beforeAcls;
  }