public static INDArray eq(INDArray x, INDArray y, INDArray z, int... dimensions) {
        if(dimensions == null || dimensions.length == 0) {
            validateShapesNoDimCase(x,y,z);
            return Nd4j.getExecutioner().exec(new OldEqualTo(x,y,z));
        }
        return Nd4j.getExecutioner().exec(new BroadcastEqualTo(x,y,z,dimensions));
    }