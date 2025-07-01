def foreach(self, f):
        """
        Applies a function to all elements of this RDD.

        >>> def f(x): print(x)
        >>> sc.parallelize([1, 2, 3, 4, 5]).foreach(f)
        """
        f = fail_on_stopiteration(f)

        def processPartition(iterator):
            for x in iterator:
                f(x)
            return iter([])
        self.mapPartitions(processPartition).count()