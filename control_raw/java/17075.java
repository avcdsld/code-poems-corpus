public static INDArray amax(INDArray x, INDArray y, INDArray z, int... dimensions) {
        if(dimensions == null || dimensions.length == 0) {
            validateShapesNoDimCase(x,y,z);
            return Nd4j.getExecutioner().exec(new AMax(x,y,z));
        }

        return Nd4j.getExecutioner().exec(new BroadcastAMax(x,y,z,dimensions));
    }