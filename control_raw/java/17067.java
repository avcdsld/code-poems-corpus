public static INDArray lte(INDArray x, INDArray y, INDArray z, int... dimensions) {
        if(dimensions == null || dimensions.length == 0) {
            validateShapesNoDimCase(x,y,z);
            return Nd4j.getExecutioner().exec(new OldLessThanOrEqual(x,y,z));
        }

        return Nd4j.getExecutioner().exec(new BroadcastLessThanOrEqual(x,y,z,dimensions));
    }