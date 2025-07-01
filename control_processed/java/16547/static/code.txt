public static INDArrayIndex[] fillIn(int[] shape, INDArrayIndex... indexes) {
        if (shape.length == indexes.length)
            return indexes;

        INDArrayIndex[] newIndexes = new INDArrayIndex[shape.length];
        System.arraycopy(indexes, 0, newIndexes, 0, indexes.length);

        for (int i = indexes.length; i < shape.length; i++) {
            newIndexes[i] = NDArrayIndex.interval(0, shape[i]);
        }
        return newIndexes;

    }