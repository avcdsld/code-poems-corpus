def substr(self, startPos, length):
        """
        Return a :class:`Column` which is a substring of the column.

        :param startPos: start position (int or Column)
        :param length:  length of the substring (int or Column)

        >>> df.select(df.name.substr(1, 3).alias("col")).collect()
        [Row(col=u'Ali'), Row(col=u'Bob')]
        """
        if type(startPos) != type(length):
            raise TypeError(
                "startPos and length must be the same type. "
                "Got {startPos_t} and {length_t}, respectively."
                .format(
                    startPos_t=type(startPos),
                    length_t=type(length),
                ))
        if isinstance(startPos, int):
            jc = self._jc.substr(startPos, length)
        elif isinstance(startPos, Column):
            jc = self._jc.substr(startPos._jc, length._jc)
        else:
            raise TypeError("Unexpected type: %s" % type(startPos))
        return Column(jc)