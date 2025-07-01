def _get_upload_arguments(self, content_type):
        """Get required arguments for performing an upload.

        The content type returned will be determined in order of precedence:

        - The value passed in to this method (if not :data:`None`)
        - The value stored on the current blob
        - The default value ('application/octet-stream')

        :type content_type: str
        :param content_type: Type of content being uploaded (or :data:`None`).

        :rtype: tuple
        :returns: A triple of

                  * A header dictionary
                  * An object metadata dictionary
                  * The ``content_type`` as a string (according to precedence)
        """
        headers = _get_encryption_headers(self._encryption_key)
        object_metadata = self._get_writable_metadata()
        content_type = self._get_content_type(content_type)
        return headers, object_metadata, content_type