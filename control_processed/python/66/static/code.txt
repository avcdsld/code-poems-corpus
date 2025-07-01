def intersection(self, other):
        """
        Return the intersection of this RDD and another one. The output will
        not contain any duplicate elements, even if the input RDDs did.

        .. note:: This method performs a shuffle internally.

        >>> rdd1 = sc.parallelize([1, 10, 2, 3, 4, 5])
        >>> rdd2 = sc.parallelize([1, 6, 2, 3, 7, 8])
        >>> rdd1.intersection(rdd2).collect()
        [1, 2, 3]
        """
        return self.map(lambda v: (v, None)) \
            .cogroup(other.map(lambda v: (v, None))) \
            .filter(lambda k_vs: all(k_vs[1])) \
            .keys()