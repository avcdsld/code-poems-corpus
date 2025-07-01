def fold(self, zeroValue, op):
        """
        Aggregate the elements of each partition, and then the results for all
        the partitions, using a given associative function and a neutral "zero value."

        The function C{op(t1, t2)} is allowed to modify C{t1} and return it
        as its result value to avoid object allocation; however, it should not
        modify C{t2}.

        This behaves somewhat differently from fold operations implemented
        for non-distributed collections in functional languages like Scala.
        This fold operation may be applied to partitions individually, and then
        fold those results into the final result, rather than apply the fold
        to each element sequentially in some defined ordering. For functions
        that are not commutative, the result may differ from that of a fold
        applied to a non-distributed collection.

        >>> from operator import add
        >>> sc.parallelize([1, 2, 3, 4, 5]).fold(0, add)
        15
        """
        op = fail_on_stopiteration(op)

        def func(iterator):
            acc = zeroValue
            for obj in iterator:
                acc = op(acc, obj)
            yield acc
        # collecting result of mapPartitions here ensures that the copy of
        # zeroValue provided to each partition is unique from the one provided
        # to the final reduce call
        vals = self.mapPartitions(func).collect()
        return reduce(op, vals, zeroValue)