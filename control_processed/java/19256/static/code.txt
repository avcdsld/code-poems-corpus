@Override
    protected void saxpyi(long N, double alpha, INDArray X, DataBuffer pointers, INDArray Y) {
        cblas_saxpyi((int) N, (float) alpha, (FloatPointer) X.data().addressPointer(), (IntPointer) pointers.addressPointer(),
                (FloatPointer) Y.data().addressPointer());
    }