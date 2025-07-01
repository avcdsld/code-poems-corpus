public List<Acl> listDefaultBucketAcls(String bucketName) {
    // [START listDefaultBucketAcls]
    List<Acl> acls = storage.listDefaultAcls(bucketName);
    for (Acl acl : acls) {
      // do something with ACL entry
    }
    // [END listDefaultBucketAcls]
    return acls;
  }