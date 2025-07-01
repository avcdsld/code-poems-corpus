public SDVariable argmin(String name, boolean keepDims, int... dimensions) {
        return sameDiff.argmax(name, this, keepDims, dimensions);
    }