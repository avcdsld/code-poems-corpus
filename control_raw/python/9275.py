def open_file(link, session=None, stream=True):
    """
    Open local or remote file for reading.

    :type link: pip._internal.index.Link or str
    :type session: requests.Session
    :param bool stream: Try to stream if remote, default True
    :raises ValueError: If link points to a local directory.
    :return: a context manager to the opened file-like object
    """
    if not isinstance(link, six.string_types):
        try:
            link = link.url_without_fragment
        except AttributeError:
            raise ValueError("Cannot parse url from unkown type: {0!r}".format(link))

    if not is_valid_url(link) and os.path.exists(link):
        link = path_to_url(link)

    if is_file_url(link):
        # Local URL
        local_path = url_to_path(link)
        if os.path.isdir(local_path):
            raise ValueError("Cannot open directory for read: {}".format(link))
        else:
            with io.open(local_path, "rb") as local_file:
                yield local_file
    else:
        # Remote URL
        headers = {"Accept-Encoding": "identity"}
        if not session:
            from requests import Session

            session = Session()
        with session.get(link, headers=headers, stream=stream) as resp:
            try:
                raw = getattr(resp, "raw", None)
                result = raw if raw else resp
                yield result
            finally:
                if raw:
                    conn = getattr(raw, "_connection")
                    if conn is not None:
                        conn.close()
                result.close()