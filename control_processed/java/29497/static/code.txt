public Bucket getRetentionPolicy(String bucketName) throws StorageException {
    // [START storage_get_retention_policy]
    // Instantiate a Google Cloud Storage client
    Storage storage = StorageOptions.getDefaultInstance().getService();

    // The name of a bucket, e.g. "my-bucket"
    // String bucketName = "my-bucket";

    Bucket bucket = storage.get(bucketName, BucketGetOption.fields(BucketField.RETENTION_POLICY));

    System.out.println("Retention Policy for " + bucketName);
    System.out.println("Retention Period: " + bucket.getRetentionPeriod());
    if (bucket.retentionPolicyIsLocked() != null && bucket.retentionPolicyIsLocked()) {
      System.out.println("Retention Policy is locked");
    }
    if (bucket.getRetentionEffectiveTime() != null) {
      System.out.println("Effective Time: " + new Date(bucket.getRetentionEffectiveTime()));
    }
    // [END storage_get_retention_policy]
    return bucket;
  }