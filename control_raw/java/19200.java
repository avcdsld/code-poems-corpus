public static INDArray pow(INDArray ndArray, INDArray power, boolean dup) {
        INDArray result = (dup ? ndArray.ulike() : ndArray);
        return exec(new PowPairwise(ndArray, power, result));
    }