@Override
    public MultiDataSet next() {
        counter.incrementAndGet();

        INDArray[] features = new INDArray[baseFeatures.length];
        System.arraycopy(baseFeatures, 0, features, 0, baseFeatures.length);
        INDArray[] labels = new INDArray[baseLabels.length];
        System.arraycopy(baseLabels, 0, labels, 0, baseLabels.length);

        MultiDataSet ds = new MultiDataSet(features, labels);

        return ds;
    }