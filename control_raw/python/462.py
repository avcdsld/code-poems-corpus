def entries(self):
        """
        Entries of the CoordinateMatrix stored as an RDD of
        MatrixEntries.

        >>> mat = CoordinateMatrix(sc.parallelize([MatrixEntry(0, 0, 1.2),
        ...                                        MatrixEntry(6, 4, 2.1)]))
        >>> entries = mat.entries
        >>> entries.first()
        MatrixEntry(0, 0, 1.2)
        """
        # We use DataFrames for serialization of MatrixEntry entries
        # from Java, so we first convert the RDD of entries to a
        # DataFrame on the Scala/Java side. Then we map each Row in
        # the DataFrame back to a MatrixEntry on this side.
        entries_df = callMLlibFunc("getMatrixEntries", self._java_matrix_wrapper._java_model)
        entries = entries_df.rdd.map(lambda row: MatrixEntry(row[0], row[1], row[2]))
        return entries