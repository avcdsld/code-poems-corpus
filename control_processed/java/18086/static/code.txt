public SDVariable conv3d(SDVariable[] inputs, Conv3DConfig conv3DConfig) {
        Conv3D conv3D = Conv3D.builder()
                .inputFunctions(inputs)
                .conv3DConfig(conv3DConfig)
                .sameDiff(sameDiff())
                .build();

        val outputVars = conv3D.outputVariables();
        return outputVars[0];
    }