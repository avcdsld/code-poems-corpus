def read_dataset_metadata(self):
    """Read `dataset_meta` field from bucket"""
    if self.dataset_meta:
      return
    shell_call(['gsutil', 'cp',
                'gs://' + self.storage_client.bucket_name + '/'
                + 'dataset/' + self.dataset_name + '_dataset.csv',
                LOCAL_DATASET_METADATA_FILE])
    with open(LOCAL_DATASET_METADATA_FILE, 'r') as f:
      self.dataset_meta = eval_lib.DatasetMetadata(f)