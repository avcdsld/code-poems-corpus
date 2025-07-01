def text(self):
        """
        Content of the response, in unicode.

        if Response.encoding is None and chardet module is available, encoding
        will be guessed.
        """
        if hasattr(self, '_text') and self._text:
            return self._text
        if not self.content:
            return u''
        if isinstance(self.content, six.text_type):
            return self.content

        content = None
        encoding = self.encoding

        # Decode unicode from given encoding.
        try:
            content = self.content.decode(encoding, 'replace')
        except LookupError:
            # A LookupError is raised if the encoding was not found which could
            # indicate a misspelling or similar mistake.
            #
            # So we try blindly encoding.
            content = self.content.decode('utf-8', 'replace')

        self._text = content
        return content