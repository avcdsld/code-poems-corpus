def add_months(start, months):
    """
    Returns the date that is `months` months after `start`

    >>> df = spark.createDataFrame([('2015-04-08',)], ['dt'])
    >>> df.select(add_months(df.dt, 1).alias('next_month')).collect()
    [Row(next_month=datetime.date(2015, 5, 8))]
    """
    sc = SparkContext._active_spark_context
    return Column(sc._jvm.functions.add_months(_to_java_column(start), months))