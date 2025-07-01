def round(col, scale=0):
    """
    Round the given value to `scale` decimal places using HALF_UP rounding mode if `scale` >= 0
    or at integral part when `scale` < 0.

    >>> spark.createDataFrame([(2.5,)], ['a']).select(round('a', 0).alias('r')).collect()
    [Row(r=3.0)]
    """
    sc = SparkContext._active_spark_context
    return Column(sc._jvm.functions.round(_to_java_column(col), scale))