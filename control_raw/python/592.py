def normalVectorRDD(sc, numRows, numCols, numPartitions=None, seed=None):
        """
        Generates an RDD comprised of vectors containing i.i.d. samples drawn
        from the standard normal distribution.

        :param sc: SparkContext used to create the RDD.
        :param numRows: Number of Vectors in the RDD.
        :param numCols: Number of elements in each Vector.
        :param numPartitions: Number of partitions in the RDD (default: `sc.defaultParallelism`).
        :param seed: Random seed (default: a random long integer).
        :return: RDD of Vector with vectors containing i.i.d. samples ~ `N(0.0, 1.0)`.

        >>> import numpy as np
        >>> mat = np.matrix(RandomRDDs.normalVectorRDD(sc, 100, 100, seed=1).collect())
        >>> mat.shape
        (100, 100)
        >>> abs(mat.mean() - 0.0) < 0.1
        True
        >>> abs(mat.std() - 1.0) < 0.1
        True
        """
        return callMLlibFunc("normalVectorRDD", sc._jsc, numRows, numCols, numPartitions, seed)