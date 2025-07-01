public synchronized int getPredictedTotal(T predicted) {
        int total = 0;
        for (T actual : classes) {
            total += getCount(actual, predicted);
        }
        return total;
    }