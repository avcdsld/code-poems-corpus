public MultiLayerNetwork fitLabeledPoint(JavaRDD<LabeledPoint> rdd) {
        int nLayers = network.getLayerWiseConfigurations().getConfs().size();
        FeedForwardLayer ffl = (FeedForwardLayer) network.getLayerWiseConfigurations().getConf(nLayers - 1).getLayer();
        JavaRDD<DataSet> ds = MLLibUtil.fromLabeledPoint(sc, rdd, ffl.getNOut());
        return fit(ds);
    }