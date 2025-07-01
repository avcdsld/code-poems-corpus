public SDVariable layerNorm(SDVariable input, SDVariable gain, SDVariable bias, int... dimensions) {
        return layerNorm(null, input, gain, bias, dimensions);
    }