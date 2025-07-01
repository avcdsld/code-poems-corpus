def upload_from_filename(
        self, filename, content_type=None, client=None, predefined_acl=None
    ):
        """Upload this blob's contents from the content of a named file.

        The content type of the upload will be determined in order
        of precedence:

        - The value passed in to this method (if not :data:`None`)
        - The value stored on the current blob
        - The value given by ``mimetypes.guess_type``
        - The default value ('application/octet-stream')

        .. note::
           The effect of uploading to an existing blob depends on the
           "versioning" and "lifecycle" policies defined on the blob's
           bucket.  In the absence of those policies, upload will
           overwrite any existing contents.

           See the `object versioning
           <https://cloud.google.com/storage/docs/object-versioning>`_ and
           `lifecycle <https://cloud.google.com/storage/docs/lifecycle>`_
           API documents for details.

        If :attr:`user_project` is set on the bucket, bills the API request
        to that project.

        :type filename: str
        :param filename: The path to the file.

        :type content_type: str
        :param content_type: Optional type of content being uploaded.

        :type client: :class:`~google.cloud.storage.client.Client`
        :param client: (Optional) The client to use.  If not passed, falls back
                       to the ``client`` stored on the blob's bucket.

        :type predefined_acl: str
        :param predefined_acl: (Optional) predefined access control list
        """
        content_type = self._get_content_type(content_type, filename=filename)

        with open(filename, "rb") as file_obj:
            total_bytes = os.fstat(file_obj.fileno()).st_size
            self.upload_from_file(
                file_obj,
                content_type=content_type,
                client=client,
                size=total_bytes,
                predefined_acl=predefined_acl,
            )