public Pair<Double, INDArray> nn(INDArray point) {
        return nn(root, point, rect, Double.POSITIVE_INFINITY, null, 0);
    }