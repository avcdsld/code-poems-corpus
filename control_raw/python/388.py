def slice(x, start, length):
    """
    Collection function: returns an array containing  all the elements in `x` from index `start`
    (or starting from the end if `start` is negative) with the specified `length`.
    >>> df = spark.createDataFrame([([1, 2, 3],), ([4, 5],)], ['x'])
    >>> df.select(slice(df.x, 2, 2).alias("sliced")).collect()
    [Row(sliced=[2, 3]), Row(sliced=[5])]
    """
    sc = SparkContext._active_spark_context
    return Column(sc._jvm.functions.slice(_to_java_column(x), start, length))