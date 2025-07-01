def read(self, filename, binary_mode=False, size=None, offset=None):
        """Reads contents of a file to a string.

        Args:
            filename: string, a path
            binary_mode: bool, read as binary if True, otherwise text
            size: int, number of bytes or characters to read, otherwise
                read all the contents of the file from the offset
            offset: int, offset into file to read from, otherwise read
                from the very beginning

        Returns:
            Subset of the contents of the file as a string or bytes.
        """
        s3 = boto3.resource("s3")
        bucket, path = self.bucket_and_path(filename)
        args = {}
        endpoint = 0
        if size is not None or offset is not None:
            if offset is None:
                offset = 0
            endpoint = '' if size is None else (offset + size)
            args['Range'] = 'bytes={}-{}'.format(offset, endpoint)
        try:
            stream = s3.Object(bucket, path).get(**args)['Body'].read()
        except botocore.exceptions.ClientError as exc:
            if exc.response['Error']['Code'] == '416':
                if size is not None:
                    # Asked for too much, so request just to the end. Do this
                    # in a second request so we don't check length in all cases.
                    client = boto3.client("s3")
                    obj = client.head_object(Bucket=bucket, Key=path)
                    len = obj['ContentLength']
                    endpoint = min(len, offset + size)
                if offset == endpoint:
                    # Asked for no bytes, so just return empty
                    stream = b''
                else:
                    args['Range'] = 'bytes={}-{}'.format(offset, endpoint)
                    stream = s3.Object(bucket, path).get(**args)['Body'].read()
            else:
                raise
        if binary_mode:
            return bytes(stream)
        else:
            return stream.decode('utf-8')