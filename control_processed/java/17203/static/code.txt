@Override
    public InputType getOutputType(InputType... inputType) throws InvalidKerasConfigurationException {
        if (inputType.length > 1)
            throw new InvalidKerasConfigurationException(
                    "Keras SpatialDropout layer accepts only one input (received " + inputType.length + ")");
        return this.getSpatialDropoutLayer().getOutputType(-1, inputType[0]);
    }