def _download_from_s3(bucket, key, version=None):
        """
        Download a file from given S3 location, if available.

        Parameters
        ----------
        bucket : str
            S3 Bucket name

        key : str
            S3 Bucket Key aka file path

        version : str
            Optional Version ID of the file

        Returns
        -------
        str
            Contents of the file that was downloaded

        Raises
        ------
        botocore.exceptions.ClientError if we were unable to download the file from S3
        """

        s3 = boto3.client('s3')

        extra_args = {}
        if version:
            extra_args["VersionId"] = version

        with tempfile.TemporaryFile() as fp:
            try:
                s3.download_fileobj(
                    bucket, key, fp,
                    ExtraArgs=extra_args)

                # go to start of file
                fp.seek(0)

                # Read and return all the contents
                return fp.read()

            except botocore.exceptions.ClientError:
                LOG.error("Unable to download Swagger document from S3 Bucket=%s Key=%s Version=%s",
                          bucket, key, version)
                raise