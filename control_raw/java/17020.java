private static LabeledPoint toLabeledPoint(DataSet point) {
        if (!point.getFeatures().isVector()) {
            throw new IllegalArgumentException("Feature matrix must be a vector");
        }

        Vector features = toVector(point.getFeatures().dup());

        double label = Nd4j.getBlasWrapper().iamax(point.getLabels());
        return new LabeledPoint(label, features);
    }