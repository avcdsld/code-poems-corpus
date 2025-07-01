def createDataFrame(self, data, schema=None, samplingRatio=None, verifySchema=True):
        """
        Creates a :class:`DataFrame` from an :class:`RDD`, a list or a :class:`pandas.DataFrame`.

        When ``schema`` is a list of column names, the type of each column
        will be inferred from ``data``.

        When ``schema`` is ``None``, it will try to infer the schema (column names and types)
        from ``data``, which should be an RDD of :class:`Row`,
        or :class:`namedtuple`, or :class:`dict`.

        When ``schema`` is :class:`pyspark.sql.types.DataType` or a datatype string it must match
        the real data, or an exception will be thrown at runtime. If the given schema is not
        :class:`pyspark.sql.types.StructType`, it will be wrapped into a
        :class:`pyspark.sql.types.StructType` as its only field, and the field name will be "value",
        each record will also be wrapped into a tuple, which can be converted to row later.

        If schema inference is needed, ``samplingRatio`` is used to determined the ratio of
        rows used for schema inference. The first row will be used if ``samplingRatio`` is ``None``.

        :param data: an RDD of any kind of SQL data representation(e.g. :class:`Row`,
            :class:`tuple`, ``int``, ``boolean``, etc.), or :class:`list`, or
            :class:`pandas.DataFrame`.
        :param schema: a :class:`pyspark.sql.types.DataType` or a datatype string or a list of
            column names, default is None.  The data type string format equals to
            :class:`pyspark.sql.types.DataType.simpleString`, except that top level struct type can
            omit the ``struct<>`` and atomic types use ``typeName()`` as their format, e.g. use
            ``byte`` instead of ``tinyint`` for :class:`pyspark.sql.types.ByteType`.
            We can also use ``int`` as a short name for :class:`pyspark.sql.types.IntegerType`.
        :param samplingRatio: the sample ratio of rows used for inferring
        :param verifySchema: verify data types of every row against schema.
        :return: :class:`DataFrame`

        .. versionchanged:: 2.0
           The ``schema`` parameter can be a :class:`pyspark.sql.types.DataType` or a
           datatype string after 2.0.
           If it's not a :class:`pyspark.sql.types.StructType`, it will be wrapped into a
           :class:`pyspark.sql.types.StructType` and each record will also be wrapped into a tuple.

        .. versionchanged:: 2.1
           Added verifySchema.

        >>> l = [('Alice', 1)]
        >>> sqlContext.createDataFrame(l).collect()
        [Row(_1=u'Alice', _2=1)]
        >>> sqlContext.createDataFrame(l, ['name', 'age']).collect()
        [Row(name=u'Alice', age=1)]

        >>> d = [{'name': 'Alice', 'age': 1}]
        >>> sqlContext.createDataFrame(d).collect()
        [Row(age=1, name=u'Alice')]

        >>> rdd = sc.parallelize(l)
        >>> sqlContext.createDataFrame(rdd).collect()
        [Row(_1=u'Alice', _2=1)]
        >>> df = sqlContext.createDataFrame(rdd, ['name', 'age'])
        >>> df.collect()
        [Row(name=u'Alice', age=1)]

        >>> from pyspark.sql import Row
        >>> Person = Row('name', 'age')
        >>> person = rdd.map(lambda r: Person(*r))
        >>> df2 = sqlContext.createDataFrame(person)
        >>> df2.collect()
        [Row(name=u'Alice', age=1)]

        >>> from pyspark.sql.types import *
        >>> schema = StructType([
        ...    StructField("name", StringType(), True),
        ...    StructField("age", IntegerType(), True)])
        >>> df3 = sqlContext.createDataFrame(rdd, schema)
        >>> df3.collect()
        [Row(name=u'Alice', age=1)]

        >>> sqlContext.createDataFrame(df.toPandas()).collect()  # doctest: +SKIP
        [Row(name=u'Alice', age=1)]
        >>> sqlContext.createDataFrame(pandas.DataFrame([[1, 2]])).collect()  # doctest: +SKIP
        [Row(0=1, 1=2)]

        >>> sqlContext.createDataFrame(rdd, "a: string, b: int").collect()
        [Row(a=u'Alice', b=1)]
        >>> rdd = rdd.map(lambda row: row[1])
        >>> sqlContext.createDataFrame(rdd, "int").collect()
        [Row(value=1)]
        >>> sqlContext.createDataFrame(rdd, "boolean").collect() # doctest: +IGNORE_EXCEPTION_DETAIL
        Traceback (most recent call last):
            ...
        Py4JJavaError: ...
        """
        return self.sparkSession.createDataFrame(data, schema, samplingRatio, verifySchema)