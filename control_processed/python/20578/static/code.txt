def listdir(self, path, start_time=None, end_time=None, return_key=False):
        """
        Get an iterable with S3 folder contents.
        Iterable contains paths relative to queried path.
        :param path: URL for target S3 location
        :param start_time: Optional argument to list files with modified (offset aware) datetime after start_time
        :param end_time: Optional argument to list files with modified (offset aware) datetime before end_time
        :param return_key: Optional argument, when set to True will return boto3's ObjectSummary (instead of the filename)
        """
        (bucket, key) = self._path_to_bucket_and_key(path)

        # grab and validate the bucket
        s3_bucket = self.s3.Bucket(bucket)

        key_path = self._add_path_delimiter(key)
        key_path_len = len(key_path)
        for item in s3_bucket.objects.filter(Prefix=key_path):
            last_modified_date = item.last_modified
            if (
                # neither are defined, list all
                (not start_time and not end_time) or
                # start defined, after start
                (start_time and not end_time and start_time < last_modified_date) or
                # end defined, prior to end
                (not start_time and end_time and last_modified_date < end_time) or
                (start_time and end_time and start_time <
                 last_modified_date < end_time)  # both defined, between
            ):
                if return_key:
                    yield item
                else:
                    yield self._add_path_delimiter(path) + item.key[key_path_len:]