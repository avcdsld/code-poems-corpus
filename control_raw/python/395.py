def get_json_object(col, path):
    """
    Extracts json object from a json string based on json path specified, and returns json string
    of the extracted json object. It will return null if the input json string is invalid.

    :param col: string column in json format
    :param path: path to the json object to extract

    >>> data = [("1", '''{"f1": "value1", "f2": "value2"}'''), ("2", '''{"f1": "value12"}''')]
    >>> df = spark.createDataFrame(data, ("key", "jstring"))
    >>> df.select(df.key, get_json_object(df.jstring, '$.f1').alias("c0"), \\
    ...                   get_json_object(df.jstring, '$.f2').alias("c1") ).collect()
    [Row(key=u'1', c0=u'value1', c1=u'value2'), Row(key=u'2', c0=u'value12', c1=None)]
    """
    sc = SparkContext._active_spark_context
    jc = sc._jvm.functions.get_json_object(_to_java_column(col), path)
    return Column(jc)