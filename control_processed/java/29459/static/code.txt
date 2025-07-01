public Blob batch(String bucketName, String blobName1, String blobName2) {
    // [START batch]
    StorageBatch batch = storage.batch();
    BlobId firstBlob = BlobId.of(bucketName, blobName1);
    BlobId secondBlob = BlobId.of(bucketName, blobName2);
    batch
        .delete(firstBlob)
        .notify(
            new BatchResult.Callback<Boolean, StorageException>() {
              public void success(Boolean result) {
                // deleted successfully
              }

              public void error(StorageException exception) {
                // delete failed
              }
            });
    batch.update(BlobInfo.newBuilder(secondBlob).setContentType("text/plain").build());
    StorageBatchResult<Blob> result = batch.get(secondBlob);
    batch.submit();
    Blob blob = result.get(); // returns get result or throws StorageException
    // [END batch]
    return blob;
  }