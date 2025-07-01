public static INDArrayIndex[] resolve(INDArrayIndex[] allIndex, INDArrayIndex... intendedIndexes) {

        int numNewAxes = numNewAxis(intendedIndexes);
        INDArrayIndex[] all = new INDArrayIndex[allIndex.length + numNewAxes];
        Arrays.fill(all, NDArrayIndex.all());
        for (int i = 0; i < allIndex.length; i++) {
            //collapse single length indexes in to point indexes
            if (i >= intendedIndexes.length)
                break;

            if (intendedIndexes[i] instanceof NDArrayIndex) {
                NDArrayIndex idx = (NDArrayIndex) intendedIndexes[i];
                if (idx.indices.length == 1)
                    intendedIndexes[i] = new PointIndex(idx.indices[0]);
            }
            all[i] = intendedIndexes[i];
        }

        return all;
    }