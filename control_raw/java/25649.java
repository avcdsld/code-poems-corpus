protected static SparseMatrix allocateCSRMatrix(SparseMatrixDimensions sparseMatrixDimensions) {
        // Number of rows in non-zero elements matrix
        final int dataRowsNumber = (int) (sparseMatrixDimensions._nonZeroElementsCount / SPARSE_MATRIX_DIM);
        final int dataLastRowSize = (int)(sparseMatrixDimensions._nonZeroElementsCount % SPARSE_MATRIX_DIM);
        //Number of rows in matrix with row indices
        final int rowIndicesRowsNumber = (int)(sparseMatrixDimensions._rowHeadersCount / SPARSE_MATRIX_DIM);
        final int rowIndicesLastRowSize = (int)(sparseMatrixDimensions._rowHeadersCount % SPARSE_MATRIX_DIM);
        // Number of rows in matrix with column indices of sparse matrix non-zero elements
        // There is one column index per each non-zero element, no need to recalculate.
        final int colIndicesRowsNumber = dataRowsNumber;
        final int colIndicesLastRowSize = dataLastRowSize;

        // Sparse matrix elements (non-zero elements)
        float[][] sparseData = new float[dataLastRowSize == 0 ? dataRowsNumber : dataRowsNumber + 1][];
        int iterationLimit = dataLastRowSize == 0 ? sparseData.length : sparseData.length - 1;
        for (int sparseDataRow = 0; sparseDataRow < iterationLimit; sparseDataRow++) {
            sparseData[sparseDataRow] = malloc4f(SPARSE_MATRIX_DIM);
        }
        if (dataLastRowSize > 0) {
            sparseData[sparseData.length - 1] = malloc4f(dataLastRowSize);
        }
        // Row indices
        long[][] rowIndices = new long[rowIndicesLastRowSize == 0 ? rowIndicesRowsNumber : rowIndicesRowsNumber + 1][];
        iterationLimit = rowIndicesLastRowSize == 0 ? rowIndices.length : rowIndices.length - 1;
        for (int rowIndicesRow = 0; rowIndicesRow < iterationLimit; rowIndicesRow++) {
            rowIndices[rowIndicesRow] = malloc8(SPARSE_MATRIX_DIM);
        }
        if (rowIndicesLastRowSize > 0) {
            rowIndices[rowIndices.length - 1] = malloc8(rowIndicesLastRowSize);
        }

        // Column indices
        int[][] colIndices = new int[colIndicesLastRowSize == 0 ? colIndicesRowsNumber : colIndicesRowsNumber + 1][];
        iterationLimit = colIndicesLastRowSize == 0 ? colIndices.length : colIndices.length - 1;
        for (int colIndicesRow = 0; colIndicesRow < iterationLimit; colIndicesRow++) {
            colIndices[colIndicesRow] = malloc4(SPARSE_MATRIX_DIM);
        }
        if (colIndicesLastRowSize > 0) {
            colIndices[colIndices.length - 1] = malloc4(colIndicesLastRowSize);
        }

        // Wrap backing arrays into a SparseMatrix object and return them
        return new SparseMatrix(sparseData, rowIndices, colIndices);
    }