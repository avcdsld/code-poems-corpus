@Override
    public void rnnSetPreviousState(Map<String, INDArray> stateMap) {
        this.stateMap.clear();
        this.stateMap.putAll(stateMap);
    }