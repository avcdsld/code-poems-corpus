@Override
    public Pointer getPointer(INDArray array, CudaContext context) {
        //    DataBuffer buffer = array.data().originalDataBuffer() == null ? array.data() : array.data().originalDataBuffer();
        if (array.isEmpty())
            return null;

        return memoryHandler.getDevicePointer(array.data(), context);
    }