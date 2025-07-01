public static void validateOutputLayerConfiguration(String layerName, long nOut, boolean isLossLayer, IActivation activation, ILossFunction lossFunction){
        //nOut = 1 + softmax
        if(!isLossLayer && nOut == 1 && activation instanceof ActivationSoftmax){   //May not have valid nOut for LossLayer
            throw new DL4JInvalidConfigException("Invalid output layer configuration for layer \"" + layerName + "\": Softmax + nOut=1 networks " +
                    "are not supported. Softmax cannot be used with nOut=1 as the output will always be exactly 1.0 " +
                    "regardless of the input. " + COMMON_MSG);
        }

        //loss function required probability, but activation is outside 0-1 range
        if(lossFunctionExpectsProbability(lossFunction) && activationExceedsZeroOneRange(activation, isLossLayer)){
            throw new DL4JInvalidConfigException("Invalid output layer configuration for layer \"" + layerName + "\": loss function " + lossFunction +
                    " expects activations to be in the range 0 to 1 (probabilities) but activation function " + activation +
                    " does not bound values to this 0 to 1 range. This indicates a likely invalid network configuration. " + COMMON_MSG);
        }

        //Common mistake: softmax + xent
        if(activation instanceof ActivationSoftmax && lossFunction instanceof LossBinaryXENT){
            throw new DL4JInvalidConfigException("Invalid output layer configuration for layer \"" + layerName + "\": softmax activation function in combination " +
                    "with LossBinaryXENT (binary cross entropy loss function). For multi-class classification, use softmax + " +
                    "MCXENT (multi-class cross entropy); for binary multi-label classification, use sigmoid + XENT. " + COMMON_MSG);
        }

        //Common mistake: sigmoid + mcxent
        if(activation instanceof ActivationSigmoid && lossFunction instanceof LossMCXENT){
            throw new DL4JInvalidConfigException("Invalid output layer configuration for layer \"" + layerName + "\": sigmoid activation function in combination " +
                    "with LossMCXENT (multi-class cross entropy loss function). For multi-class classification, use softmax + " +
                    "MCXENT (multi-class cross entropy); for binary multi-label classification, use sigmoid + XENT. " + COMMON_MSG);
        }
    }