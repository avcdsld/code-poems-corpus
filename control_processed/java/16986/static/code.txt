static INDArray createMask(DataType dataType, long[] shape){
        switch (shape.length){
            case 2: // FF-Type input
                return Nd4j.ones(dataType,shape[0], 1);
            case 3: // RNN-Type input
                return Nd4j.ones(dataType, shape[0], shape[2]);
            case 4: //CNN input
                return Nd4j.ones(dataType, shape[0], 1, 1, 1);
            default:
                Preconditions.throwEx("Can not create all-ones-mask for given input shape %s.", Arrays.toString(shape));
                return null;
        }
    }