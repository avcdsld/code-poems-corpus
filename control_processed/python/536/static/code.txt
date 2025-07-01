def tables(self, dbName=None):
        """Returns a :class:`DataFrame` containing names of tables in the given database.

        If ``dbName`` is not specified, the current database will be used.

        The returned DataFrame has two columns: ``tableName`` and ``isTemporary``
        (a column with :class:`BooleanType` indicating if a table is a temporary one or not).

        :param dbName: string, name of the database to use.
        :return: :class:`DataFrame`

        >>> sqlContext.registerDataFrameAsTable(df, "table1")
        >>> df2 = sqlContext.tables()
        >>> df2.filter("tableName = 'table1'").first()
        Row(database=u'', tableName=u'table1', isTemporary=True)
        """
        if dbName is None:
            return DataFrame(self._ssql_ctx.tables(), self)
        else:
            return DataFrame(self._ssql_ctx.tables(dbName), self)