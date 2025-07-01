@Override
    public InputPreProcessor getInputPreprocessor(InputType... inputType) throws InvalidKerasConfigurationException {
        if (inputType.length > 1)
            throw new InvalidKerasConfigurationException(
                    "Keras SimpleRnn layer accepts only one input (received " + inputType.length + ")");

        return InputTypeUtil.getPreprocessorForInputTypeRnnLayers(inputType[0], layerName);
    }