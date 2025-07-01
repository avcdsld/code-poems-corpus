@Override
    public void gemv(char order, char transA, double alpha, INDArray A, INDArray X, double beta, INDArray Y) {
        if (Nd4j.getExecutioner().getProfilingMode() == OpExecutioner.ProfilingMode.ALL)
            OpProfiler.getInstance().processBlasCall(false, A, X, Y);

        if (A.isSparse() && !X.isSparse()) {
            Nd4j.getSparseBlasWrapper().level2().gemv(order, transA, alpha, A, X, beta, Y);
            return;
        }

        GemvParameters parameters = new GemvParameters(A, X, Y);
        if (A.data().dataType() == DataType.DOUBLE) {
            DefaultOpExecutioner.validateDataType(DataType.DOUBLE, parameters.getA(), parameters.getX(),
                            parameters.getY());
            dgemv(order, parameters.getAOrdering(), parameters.getM(), parameters.getN(), alpha, parameters.getA(),
                            parameters.getLda(), parameters.getX(), parameters.getIncx(), beta, parameters.getY(),
                            parameters.getIncy());
        } else if (A.data().dataType() == DataType.FLOAT){
            DefaultOpExecutioner.validateDataType(DataType.FLOAT, parameters.getA(), parameters.getX(),
                            parameters.getY());
            sgemv(order, parameters.getAOrdering(), parameters.getM(), parameters.getN(), (float) alpha,
                            parameters.getA(), parameters.getLda(), parameters.getX(), parameters.getIncx(),
                            (float) beta, parameters.getY(), parameters.getIncy());
        } else if (A.data().dataType() == DataType.HALF) {
            DefaultOpExecutioner.validateDataType(DataType.HALF, parameters.getA(), parameters.getX(),
                    parameters.getY());

            // TODO: provide optimized GEMV kernel eventually
            val fA = parameters.getA().castTo(DataType.FLOAT);
            val fX = parameters.getX().castTo(DataType.FLOAT);
            val fY = parameters.getY().castTo(DataType.FLOAT);

            sgemv(order, parameters.getAOrdering(), parameters.getM(), parameters.getN(), (float) alpha,
                    fA, parameters.getLda(), fX, parameters.getIncx(),
                    (float) beta, fY, parameters.getIncy());

            Y.assign(fY);
        } else {
            throw new ND4JIllegalStateException("Unsupported data type " + A.dataType());
        }

        OpExecutionerUtil.checkForAny(Y);
    }