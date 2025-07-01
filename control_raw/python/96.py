def reduceByKeyLocally(self, func):
        """
        Merge the values for each key using an associative and commutative reduce function, but
        return the results immediately to the master as a dictionary.

        This will also perform the merging locally on each mapper before
        sending results to a reducer, similarly to a "combiner" in MapReduce.

        >>> from operator import add
        >>> rdd = sc.parallelize([("a", 1), ("b", 1), ("a", 1)])
        >>> sorted(rdd.reduceByKeyLocally(add).items())
        [('a', 2), ('b', 1)]
        """
        func = fail_on_stopiteration(func)

        def reducePartition(iterator):
            m = {}
            for k, v in iterator:
                m[k] = func(m[k], v) if k in m else v
            yield m

        def mergeMaps(m1, m2):
            for k, v in m2.items():
                m1[k] = func(m1[k], v) if k in m1 else v
            return m1
        return self.mapPartitions(reducePartition).reduce(mergeMaps)