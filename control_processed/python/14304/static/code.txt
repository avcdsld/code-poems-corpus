def enable_logging(self, bucket_name, object_prefix=""):
        """Enable access logging for this bucket.

        See https://cloud.google.com/storage/docs/access-logs

        :type bucket_name: str
        :param bucket_name: name of bucket in which to store access logs

        :type object_prefix: str
        :param object_prefix: prefix for access log filenames
        """
        info = {"logBucket": bucket_name, "logObjectPrefix": object_prefix}
        self._patch_property("logging", info)