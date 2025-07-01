public static INDArray ndArrayDimFromInt(int... dimensions){
        if (dimensions == null || dimensions.length == 0)
            return Nd4j.empty(DataType.INT);
        else
            return Nd4j.createFromArray(dimensions);
    }