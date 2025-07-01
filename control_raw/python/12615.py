def _get_part_reader(self, headers: 'CIMultiDictProxy[str]') -> Any:
        """Dispatches the response by the `Content-Type` header, returning
        suitable reader instance.

        :param dict headers: Response headers
        """
        ctype = headers.get(CONTENT_TYPE, '')
        mimetype = parse_mimetype(ctype)

        if mimetype.type == 'multipart':
            if self.multipart_reader_cls is None:
                return type(self)(headers, self._content)
            return self.multipart_reader_cls(
                headers, self._content, _newline=self._newline
            )
        else:
            return self.part_reader_cls(
                self._boundary, headers, self._content, _newline=self._newline
            )