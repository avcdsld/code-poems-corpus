@Override
    public void fit(org.nd4j.linalg.dataset.api.DataSet data) {
        fit(data.getFeatures(), data.getLabels(), data.getFeaturesMaskArray(), data.getLabelsMaskArray());
    }