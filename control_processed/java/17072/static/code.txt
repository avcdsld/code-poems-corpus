public static INDArray sub(INDArray x, INDArray y, INDArray z, int... dimensions) {
        if(dimensions == null || dimensions.length == 0) {
            validateShapesNoDimCase(x,y,z);
            return Nd4j.getExecutioner().exec(new OldSubOp(x,y,z));
        }

        return Nd4j.getExecutioner().exec(new BroadcastSubOp(x,y,z,dimensions));
    }