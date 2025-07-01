def map(self, f, preservesPartitioning=False):
        """
        Return a new RDD by applying a function to each element of this RDD.

        >>> rdd = sc.parallelize(["b", "a", "c"])
        >>> sorted(rdd.map(lambda x: (x, 1)).collect())
        [('a', 1), ('b', 1), ('c', 1)]
        """
        def func(_, iterator):
            return map(fail_on_stopiteration(f), iterator)
        return self.mapPartitionsWithIndex(func, preservesPartitioning)