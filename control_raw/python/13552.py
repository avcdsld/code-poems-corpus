def mean(self, **kwargs):
        """Returns the mean for each numerical column or row.

        Return:
            A new QueryCompiler object containing the mean from each numerical column or
            row.
        """
        if self._is_transposed:
            kwargs["axis"] = kwargs.get("axis", 0) ^ 1
            return self.transpose().mean(**kwargs)
        # Pandas default is 0 (though not mentioned in docs)
        axis = kwargs.get("axis", 0)
        sums = self.sum(**kwargs)
        counts = self.count(axis=axis, numeric_only=kwargs.get("numeric_only", None))
        if sums._is_transposed and counts._is_transposed:
            sums = sums.transpose()
            counts = counts.transpose()
        result = sums.binary_op("truediv", counts, axis=axis)
        return result.transpose() if axis == 0 else result