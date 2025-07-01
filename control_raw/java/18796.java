private INDArray gaussianRandomMatrix(long[] shape, Random rng){
        Nd4j.checkShapeValues(shape);
        INDArray res = Nd4j.create(shape);

        GaussianDistribution op1 = new GaussianDistribution(res, 0.0, 1.0 / Math.sqrt(shape[0]));
        Nd4j.getExecutioner().exec(op1, rng);
        return res;
    }