public InputType getOutputType(InputType... inputType) throws InvalidKerasConfigurationException {
        if (inputType.length > 1)
            throw new InvalidKerasConfigurationException(
                    "Keras SameDiff layer accepts only one input (received " + inputType.length + ")");
        return this.getSameDiffLayer().getOutputType(-1, inputType[0]);
    }