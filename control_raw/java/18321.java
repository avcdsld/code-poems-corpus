@Override
    public DataSet get(int i) {
        if (i >= numExamples() || i < 0)
            throw new IllegalArgumentException("invalid example number: must be 0 to " + (numExamples()-1) + ", got " + i);
        if (i == 0 && numExamples() == 1)
            return this;
        return new DataSet(getHelper(features,i), getHelper(labels, i), getHelper(featuresMask,i), getHelper(labelsMask,i));
    }