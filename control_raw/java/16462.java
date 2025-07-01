public void scoomv(char transA, int M, DataBuffer values, DataBuffer rowInd, DataBuffer colInd, int nnz, INDArray x, INDArray y){
        mkl_cspblas_scoogemv(
                Character.toString(transA),
                (IntPointer) Nd4j.createBuffer(new int[]{M}).addressPointer(),
                (FloatPointer) values.addressPointer(),
                (IntPointer) rowInd.addressPointer(),
                (IntPointer) colInd.addressPointer(),
                (IntPointer) Nd4j.createBuffer(new int[]{nnz}).addressPointer(),
                (FloatPointer) x.data().addressPointer(),
                (FloatPointer)y.data().addressPointer());
    }