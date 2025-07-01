def _do_download(
        self, transport, file_obj, download_url, headers, start=None, end=None
    ):
        """Perform a download without any error handling.

        This is intended to be called by :meth:`download_to_file` so it can
        be wrapped with error handling / remapping.

        :type transport:
            :class:`~google.auth.transport.requests.AuthorizedSession`
        :param transport: The transport (with credentials) that will
                          make authenticated requests.

        :type file_obj: file
        :param file_obj: A file handle to which to write the blob's data.

        :type download_url: str
        :param download_url: The URL where the media can be accessed.

        :type headers: dict
        :param headers: Optional headers to be sent with the request(s).

        :type start: int
        :param start: Optional, the first byte in a range to be downloaded.

        :type end: int
        :param end: Optional, The last byte in a range to be downloaded.
        """
        if self.chunk_size is None:
            download = Download(
                download_url, stream=file_obj, headers=headers, start=start, end=end
            )
            download.consume(transport)
        else:
            download = ChunkedDownload(
                download_url,
                self.chunk_size,
                file_obj,
                headers=headers,
                start=start if start else 0,
                end=end,
            )

            while not download.finished:
                download.consume_next_chunk(transport)