def transpose(self):
        """
        Transpose this BlockMatrix. Returns a new BlockMatrix
        instance sharing the same underlying data. Is a lazy operation.

        >>> blocks = sc.parallelize([((0, 0), Matrices.dense(3, 2, [1, 2, 3, 4, 5, 6])),
        ...                          ((1, 0), Matrices.dense(3, 2, [7, 8, 9, 10, 11, 12]))])
        >>> mat = BlockMatrix(blocks, 3, 2)

        >>> mat_transposed = mat.transpose()
        >>> mat_transposed.toLocalMatrix()
        DenseMatrix(2, 6, [1.0, 4.0, 2.0, 5.0, 3.0, 6.0, 7.0, 10.0, 8.0, 11.0, 9.0, 12.0], 0)
        """
        java_transposed_matrix = self._java_matrix_wrapper.call("transpose")
        return BlockMatrix(java_transposed_matrix, self.colsPerBlock, self.rowsPerBlock)