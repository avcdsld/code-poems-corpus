@Override
    public double f1Score(INDArray examples, INDArray labels) {
        if (examples.rank() == 3)
            examples = TimeSeriesUtils.reshape3dTo2d(examples, LayerWorkspaceMgr.noWorkspaces(), ArrayType.ACTIVATIONS);
        if (labels.rank() == 3)
            labels = TimeSeriesUtils.reshape3dTo2d(labels, LayerWorkspaceMgr.noWorkspaces(), ArrayType.ACTIVATIONS);
        return super.f1Score(examples, labels);
    }