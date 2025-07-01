public static ComputationGraph toComputationGraph(MultiLayerNetwork net) {

        //We rely heavily here on the fact that the topological sort order - and hence the layout of parameters - is
        // by definition the identical for a MLN and "single stack" computation graph. This also has to hold
        // for the updater state...

        ComputationGraphConfiguration.GraphBuilder b = new NeuralNetConfiguration.Builder()
                .dataType(net.getLayerWiseConfigurations().getDataType())
                .graphBuilder();

        MultiLayerConfiguration origConf = net.getLayerWiseConfigurations().clone();


        int layerIdx = 0;
        String lastLayer = "in";
        b.addInputs("in");
        for (NeuralNetConfiguration c : origConf.getConfs()) {
            String currLayer = String.valueOf(layerIdx);

            InputPreProcessor preproc = origConf.getInputPreProcess(layerIdx);
            b.addLayer(currLayer, c.getLayer(), preproc, lastLayer);

            lastLayer = currLayer;
            layerIdx++;
        }
        b.setOutputs(lastLayer);

        ComputationGraphConfiguration conf = b.build();

        ComputationGraph cg = new ComputationGraph(conf);
        cg.init();

        cg.setParams(net.params());

        //Also copy across updater state:
        INDArray updaterState = net.getUpdater().getStateViewArray();
        if (updaterState != null) {
            cg.getUpdater().getUpdaterStateViewArray()
                    .assign(updaterState);
        }

        return cg;
    }