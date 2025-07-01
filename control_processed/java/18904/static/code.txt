public Set<String> missingTensorflowOps() {
        Set<String> copy = new HashSet<>(tensorflowOpDescriptors.keySet());
        copy.removeAll(tensorFlowNames.keySet());
        return copy;
    }