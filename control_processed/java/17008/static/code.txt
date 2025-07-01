public static INDArray toMatrix(Matrix arr) {

        // we assume that Matrix always has F order
        return Nd4j.create(arr.toArray(), new int[] {arr.numRows(), arr.numCols()}, 'f');
    }