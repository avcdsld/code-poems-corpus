public static AllocationShape buildAllocationShape(INDArray array) {
        AllocationShape shape = new AllocationShape();
        shape.setDataType(array.data().dataType());
        shape.setLength(array.length());
        shape.setDataType(array.data().dataType());

        return shape;
    }