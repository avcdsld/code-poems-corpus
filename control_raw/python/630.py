def orc(self, path):
        """Loads a ORC file stream, returning the result as a :class:`DataFrame`.

        .. note:: Evolving.

        >>> orc_sdf = spark.readStream.schema(sdf_schema).orc(tempfile.mkdtemp())
        >>> orc_sdf.isStreaming
        True
        >>> orc_sdf.schema == sdf_schema
        True
        """
        if isinstance(path, basestring):
            return self._df(self._jreader.orc(path))
        else:
            raise TypeError("path can be only a single string")