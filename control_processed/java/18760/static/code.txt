@Override
    public void copy(long n, DataBuffer x, int offsetX, int incrX, DataBuffer y, int offsetY, int incrY) {


        if (supportsDataBufferL1Ops()) {
            if (x.dataType() == DataType.DOUBLE) {
                dcopy(n, x, offsetX, incrX, y, offsetY, incrY);
            } else {
                scopy(n, x, offsetX, incrX, y, offsetY, incrY);
            }
        } else {
            long[] shapex = {1, n};
            long[] shapey = {1, n};
            long[] stridex = {incrX, incrX};
            long[] stridey = {incrY, incrY};
            INDArray arrX = Nd4j.create(x, shapex, stridex, offsetX, 'c');
            INDArray arrY = Nd4j.create(x, shapey, stridey, offsetY, 'c');
            copy(arrX, arrY);
        }
    }