def poissonVectorRDD(sc, mean, numRows, numCols, numPartitions=None, seed=None):
        """
        Generates an RDD comprised of vectors containing i.i.d. samples drawn
        from the Poisson distribution with the input mean.

        :param sc: SparkContext used to create the RDD.
        :param mean: Mean, or lambda, for the Poisson distribution.
        :param numRows: Number of Vectors in the RDD.
        :param numCols: Number of elements in each Vector.
        :param numPartitions: Number of partitions in the RDD (default: `sc.defaultParallelism`)
        :param seed: Random seed (default: a random long integer).
        :return: RDD of Vector with vectors containing i.i.d. samples ~ Pois(mean).

        >>> import numpy as np
        >>> mean = 100.0
        >>> rdd = RandomRDDs.poissonVectorRDD(sc, mean, 100, 100, seed=1)
        >>> mat = np.mat(rdd.collect())
        >>> mat.shape
        (100, 100)
        >>> abs(mat.mean() - mean) < 0.5
        True
        >>> from math import sqrt
        >>> abs(mat.std() - sqrt(mean)) < 0.5
        True
        """
        return callMLlibFunc("poissonVectorRDD", sc._jsc, float(mean), numRows, numCols,
                             numPartitions, seed)