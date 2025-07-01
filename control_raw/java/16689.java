public static INDArray concat(INDArray[] history) {
        INDArray arr = Nd4j.concat(0, history);
        return arr;
    }