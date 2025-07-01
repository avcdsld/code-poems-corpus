def parse_statements(self, end_tokens, drop_needle=False):
        """Parse multiple statements into a list until one of the end tokens
        is reached.  This is used to parse the body of statements as it also
        parses template data if appropriate.  The parser checks first if the
        current token is a colon and skips it if there is one.  Then it checks
        for the block end and parses until if one of the `end_tokens` is
        reached.  Per default the active token in the stream at the end of
        the call is the matched end token.  If this is not wanted `drop_needle`
        can be set to `True` and the end token is removed.
        """
        # the first token may be a colon for python compatibility
        self.stream.skip_if('colon')

        # in the future it would be possible to add whole code sections
        # by adding some sort of end of statement token and parsing those here.
        self.stream.expect('block_end')
        result = self.subparse(end_tokens)

        # we reached the end of the template too early, the subparser
        # does not check for this, so we do that now
        if self.stream.current.type == 'eof':
            self.fail_eof(end_tokens)

        if drop_needle:
            next(self.stream)
        return result