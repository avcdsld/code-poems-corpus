@Override
    public void scal(long N, double alpha, INDArray X) {
        switch (X.data().dataType()) {
            case DOUBLE:
                dscal(N, alpha, X, 1);
                break;
            case FLOAT:
                sscal(N, alpha, X, 1);
                break;
            case HALF:
                hscal(N, alpha, X, 1);
                break;
            default:
                throw new UnsupportedOperationException();
        }

    }