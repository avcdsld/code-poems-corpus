def groupByKeyAndWindow(self, windowDuration, slideDuration, numPartitions=None):
        """
        Return a new DStream by applying `groupByKey` over a sliding window.
        Similar to `DStream.groupByKey()`, but applies it over a sliding window.

        @param windowDuration: width of the window; must be a multiple of this DStream's
                              batching interval
        @param slideDuration:  sliding interval of the window (i.e., the interval after which
                              the new DStream will generate RDDs); must be a multiple of this
                              DStream's batching interval
        @param numPartitions:  Number of partitions of each RDD in the new DStream.
        """
        ls = self.mapValues(lambda x: [x])
        grouped = ls.reduceByKeyAndWindow(lambda a, b: a.extend(b) or a, lambda a, b: a[len(b):],
                                          windowDuration, slideDuration, numPartitions)
        return grouped.mapValues(ResultIterable)