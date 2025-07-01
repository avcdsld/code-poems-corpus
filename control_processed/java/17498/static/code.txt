public double accuracy(int outputNum) {
        assertIndex(outputNum);
        return (countTruePositive[outputNum] + countTrueNegative[outputNum]) / (double) totalCount(outputNum);
    }