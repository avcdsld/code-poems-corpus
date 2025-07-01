def exponentialRDD(sc, mean, size, numPartitions=None, seed=None):
        """
        Generates an RDD comprised of i.i.d. samples from the Exponential
        distribution with the input mean.

        :param sc: SparkContext used to create the RDD.
        :param mean: Mean, or 1 / lambda, for the Exponential distribution.
        :param size: Size of the RDD.
        :param numPartitions: Number of partitions in the RDD (default: `sc.defaultParallelism`).
        :param seed: Random seed (default: a random long integer).
        :return: RDD of float comprised of i.i.d. samples ~ Exp(mean).

        >>> mean = 2.0
        >>> x = RandomRDDs.exponentialRDD(sc, mean, 1000, seed=2)
        >>> stats = x.stats()
        >>> stats.count()
        1000
        >>> abs(stats.mean() - mean) < 0.5
        True
        >>> from math import sqrt
        >>> abs(stats.stdev() - sqrt(mean)) < 0.5
        True
        """
        return callMLlibFunc("exponentialRDD", sc._jsc, float(mean), size, numPartitions, seed)