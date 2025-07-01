def jdbc(self, url, table, column=None, lowerBound=None, upperBound=None, numPartitions=None,
             predicates=None, properties=None):
        """
        Construct a :class:`DataFrame` representing the database table named ``table``
        accessible via JDBC URL ``url`` and connection ``properties``.

        Partitions of the table will be retrieved in parallel if either ``column`` or
        ``predicates`` is specified. ``lowerBound`, ``upperBound`` and ``numPartitions``
        is needed when ``column`` is specified.

        If both ``column`` and ``predicates`` are specified, ``column`` will be used.

        .. note:: Don't create too many partitions in parallel on a large cluster;
            otherwise Spark might crash your external database systems.

        :param url: a JDBC URL of the form ``jdbc:subprotocol:subname``
        :param table: the name of the table
        :param column: the name of an integer column that will be used for partitioning;
                       if this parameter is specified, then ``numPartitions``, ``lowerBound``
                       (inclusive), and ``upperBound`` (exclusive) will form partition strides
                       for generated WHERE clause expressions used to split the column
                       ``column`` evenly
        :param lowerBound: the minimum value of ``column`` used to decide partition stride
        :param upperBound: the maximum value of ``column`` used to decide partition stride
        :param numPartitions: the number of partitions
        :param predicates: a list of expressions suitable for inclusion in WHERE clauses;
                           each one defines one partition of the :class:`DataFrame`
        :param properties: a dictionary of JDBC database connection arguments. Normally at
                           least properties "user" and "password" with their corresponding values.
                           For example { 'user' : 'SYSTEM', 'password' : 'mypassword' }
        :return: a DataFrame
        """
        if properties is None:
            properties = dict()
        jprop = JavaClass("java.util.Properties", self._spark._sc._gateway._gateway_client)()
        for k in properties:
            jprop.setProperty(k, properties[k])
        if column is not None:
            assert lowerBound is not None, "lowerBound can not be None when ``column`` is specified"
            assert upperBound is not None, "upperBound can not be None when ``column`` is specified"
            assert numPartitions is not None, \
                "numPartitions can not be None when ``column`` is specified"
            return self._df(self._jreader.jdbc(url, table, column, int(lowerBound), int(upperBound),
                                               int(numPartitions), jprop))
        if predicates is not None:
            gateway = self._spark._sc._gateway
            jpredicates = utils.toJArray(gateway, gateway.jvm.java.lang.String, predicates)
            return self._df(self._jreader.jdbc(url, table, jpredicates, jprop))
        return self._df(self._jreader.jdbc(url, table, jprop))