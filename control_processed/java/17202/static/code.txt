@Override
    public void tpsv(char order, char Uplo, char TransA, char Diag, INDArray Ap, INDArray X) {
        if (Nd4j.getExecutioner().getProfilingMode() == OpExecutioner.ProfilingMode.ALL)
            OpProfiler.getInstance().processBlasCall(false, Ap, X);

        // FIXME: int cast

        if (X.data().dataType() == DataType.DOUBLE) {
            DefaultOpExecutioner.validateDataType(DataType.DOUBLE, X, Ap);
            dtpsv(order, Uplo, TransA, Diag, (int) X.length(), Ap, X, X.stride(-1));
        } else {
            DefaultOpExecutioner.validateDataType(DataType.FLOAT, Ap, X);
            stpsv(order, Uplo, TransA, Diag, (int) X.length(), Ap, X, X.stride(-1));
        }

        OpExecutionerUtil.checkForAny(X);
    }