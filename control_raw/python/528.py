def getOrCreate(cls, sc):
        """
        Get the existing SQLContext or create a new one with given SparkContext.

        :param sc: SparkContext
        """
        if cls._instantiatedContext is None:
            jsqlContext = sc._jvm.SQLContext.getOrCreate(sc._jsc.sc())
            sparkSession = SparkSession(sc, jsqlContext.sparkSession())
            cls(sc, sparkSession, jsqlContext)
        return cls._instantiatedContext