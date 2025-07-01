def text(self, paths, wholetext=False, lineSep=None):
        """
        Loads text files and returns a :class:`DataFrame` whose schema starts with a
        string column named "value", and followed by partitioned columns if there
        are any.
        The text files must be encoded as UTF-8.

        By default, each line in the text file is a new row in the resulting DataFrame.

        :param paths: string, or list of strings, for input path(s).
        :param wholetext: if true, read each file from input path(s) as a single row.
        :param lineSep: defines the line separator that should be used for parsing. If None is
                        set, it covers all ``\\r``, ``\\r\\n`` and ``\\n``.

        >>> df = spark.read.text('python/test_support/sql/text-test.txt')
        >>> df.collect()
        [Row(value=u'hello'), Row(value=u'this')]
        >>> df = spark.read.text('python/test_support/sql/text-test.txt', wholetext=True)
        >>> df.collect()
        [Row(value=u'hello\\nthis')]
        """
        self._set_opts(wholetext=wholetext, lineSep=lineSep)
        if isinstance(paths, basestring):
            paths = [paths]
        return self._df(self._jreader.text(self._spark._sc._jvm.PythonUtils.toSeq(paths)))