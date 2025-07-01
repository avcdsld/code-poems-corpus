public List<Acl> listBucketAcls(String bucketName) {
    // [START listBucketAcls]
    List<Acl> acls = storage.listAcls(bucketName);
    for (Acl acl : acls) {
      // do something with ACL entry
    }
    // [END listBucketAcls]
    return acls;
  }