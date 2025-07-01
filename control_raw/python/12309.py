def check_etag_header(self) -> bool:
        """Checks the ``Etag`` header against requests's ``If-None-Match``.

        Returns ``True`` if the request's Etag matches and a 304 should be
        returned. For example::

            self.set_etag_header()
            if self.check_etag_header():
                self.set_status(304)
                return

        This method is called automatically when the request is finished,
        but may be called earlier for applications that override
        `compute_etag` and want to do an early check for ``If-None-Match``
        before completing the request.  The ``Etag`` header should be set
        (perhaps with `set_etag_header`) before calling this method.
        """
        computed_etag = utf8(self._headers.get("Etag", ""))
        # Find all weak and strong etag values from If-None-Match header
        # because RFC 7232 allows multiple etag values in a single header.
        etags = re.findall(
            br'\*|(?:W/)?"[^"]*"', utf8(self.request.headers.get("If-None-Match", ""))
        )
        if not computed_etag or not etags:
            return False

        match = False
        if etags[0] == b"*":
            match = True
        else:
            # Use a weak comparison when comparing entity-tags.
            def val(x: bytes) -> bytes:
                return x[2:] if x.startswith(b"W/") else x

            for etag in etags:
                if val(etag) == val(computed_etag):
                    match = True
                    break
        return match