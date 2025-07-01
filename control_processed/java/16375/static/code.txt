public InputPreProcessor getInputPreprocessor(InputType... inputType) throws InvalidKerasConfigurationException {
        if (inputType.length > 1)
            throw new InvalidKerasConfigurationException(
                    "Keras GlobalPooling layer accepts only one input (received " + inputType.length + ")");
        InputPreProcessor preprocessor;
        if (inputType[0].getType() == InputType.Type.FF && this.dimensions.length == 1) {
            preprocessor = new FeedForwardToRnnPreProcessor();
        } else {
            preprocessor = this.getGlobalPoolingLayer().getPreProcessorForInputType(inputType[0]);
        }
        return preprocessor;
    }