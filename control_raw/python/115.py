def countApprox(self, timeout, confidence=0.95):
        """
        .. note:: Experimental

        Approximate version of count() that returns a potentially incomplete
        result within a timeout, even if not all tasks have finished.

        >>> rdd = sc.parallelize(range(1000), 10)
        >>> rdd.countApprox(1000, 1.0)
        1000
        """
        drdd = self.mapPartitions(lambda it: [float(sum(1 for i in it))])
        return int(drdd.sumApprox(timeout, confidence))