public INDArray project(INDArray data){
        long[] tShape = targetShape(data.shape(), eps, components, autoMode);
        return data.mmul(getProjectionMatrix(tShape, this.rng));
    }