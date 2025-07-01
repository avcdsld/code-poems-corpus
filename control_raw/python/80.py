def treeAggregate(self, zeroValue, seqOp, combOp, depth=2):
        """
        Aggregates the elements of this RDD in a multi-level tree
        pattern.

        :param depth: suggested depth of the tree (default: 2)

        >>> add = lambda x, y: x + y
        >>> rdd = sc.parallelize([-5, -4, -3, -2, -1, 1, 2, 3, 4], 10)
        >>> rdd.treeAggregate(0, add, add)
        -5
        >>> rdd.treeAggregate(0, add, add, 1)
        -5
        >>> rdd.treeAggregate(0, add, add, 2)
        -5
        >>> rdd.treeAggregate(0, add, add, 5)
        -5
        >>> rdd.treeAggregate(0, add, add, 10)
        -5
        """
        if depth < 1:
            raise ValueError("Depth cannot be smaller than 1 but got %d." % depth)

        if self.getNumPartitions() == 0:
            return zeroValue

        def aggregatePartition(iterator):
            acc = zeroValue
            for obj in iterator:
                acc = seqOp(acc, obj)
            yield acc

        partiallyAggregated = self.mapPartitions(aggregatePartition)
        numPartitions = partiallyAggregated.getNumPartitions()
        scale = max(int(ceil(pow(numPartitions, 1.0 / depth))), 2)
        # If creating an extra level doesn't help reduce the wall-clock time, we stop the tree
        # aggregation.
        while numPartitions > scale + numPartitions / scale:
            numPartitions /= scale
            curNumPartitions = int(numPartitions)

            def mapPartition(i, iterator):
                for obj in iterator:
                    yield (i % curNumPartitions, obj)

            partiallyAggregated = partiallyAggregated \
                .mapPartitionsWithIndex(mapPartition) \
                .reduceByKey(combOp, curNumPartitions) \
                .values()

        return partiallyAggregated.reduce(combOp)