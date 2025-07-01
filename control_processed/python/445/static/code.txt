def appendBias(data):
        """
        Returns a new vector with `1.0` (bias) appended to
        the end of the input vector.
        """
        vec = _convert_to_vector(data)
        if isinstance(vec, SparseVector):
            newIndices = np.append(vec.indices, len(vec))
            newValues = np.append(vec.values, 1.0)
            return SparseVector(len(vec) + 1, newIndices, newValues)
        else:
            return _convert_to_vector(np.append(vec.toArray(), 1.0))