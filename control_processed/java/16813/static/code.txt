public INDArray[] output(boolean train, MemoryWorkspace outputWorkspace, INDArray... input) {
        return output(train, input, inputMaskArrays, labelMaskArrays, outputWorkspace);
    }