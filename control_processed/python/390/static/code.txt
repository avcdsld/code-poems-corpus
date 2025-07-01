def concat(*cols):
    """
    Concatenates multiple input columns together into a single column.
    The function works with strings, binary and compatible array columns.

    >>> df = spark.createDataFrame([('abcd','123')], ['s', 'd'])
    >>> df.select(concat(df.s, df.d).alias('s')).collect()
    [Row(s=u'abcd123')]

    >>> df = spark.createDataFrame([([1, 2], [3, 4], [5]), ([1, 2], None, [3])], ['a', 'b', 'c'])
    >>> df.select(concat(df.a, df.b, df.c).alias("arr")).collect()
    [Row(arr=[1, 2, 3, 4, 5]), Row(arr=None)]
    """
    sc = SparkContext._active_spark_context
    return Column(sc._jvm.functions.concat(_to_seq(sc, cols, _to_java_column)))