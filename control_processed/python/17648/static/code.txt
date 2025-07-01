def _parse_s3_location(location):
        """
        Parses the given location input as a S3 Location and returns the file's bucket, key and version as separate
        values. Input can be in two different formats:

        1. Dictionary with ``Bucket``, ``Key``, ``Version`` keys
        2. String of S3 URI in format ``s3://<bucket>/<key>?versionId=<version>``

        If the input is not in either of the above formats, this method will return (None, None, None) tuple for all
        the values.

        Parameters
        ----------
        location : str or dict
            Location of the S3 file

        Returns
        -------
        str
            Name of the S3 Bucket. None, if bucket value was not found
        str
            Key of the file from S3. None, if key was not provided
        str
            Optional Version ID of the file. None, if version ID is not provided
        """

        bucket, key, version = None, None, None
        if isinstance(location, dict):
            # This is a S3 Location dictionary. Just grab the fields. It is very well possible that
            # this dictionary has none of the fields we expect. Return None if the fields don't exist.
            bucket, key, version = (
                location.get("Bucket"),
                location.get("Key"),
                location.get("Version")
            )

        elif isinstance(location, string_types) and location.startswith("s3://"):
            # This is a S3 URI. Parse it using a standard URI parser to extract the components

            parsed = urlparse(location)
            query = parse_qs(parsed.query)

            bucket = parsed.netloc
            key = parsed.path.lstrip('/')  # Leading '/' messes with S3 APIs. Remove it.

            # If there is a query string that has a single versionId field,
            # set the object version and return
            if query and 'versionId' in query and len(query['versionId']) == 1:
                version = query['versionId'][0]

        return bucket, key, version