public Double getAvgDelayTime() {
        Double avgDelayTime = 0.0;
        if (items.size() != 0) {
            for (DelayStat item : items) {
                avgDelayTime += item.getDelayTime();
            }
            avgDelayTime = avgDelayTime / items.size();
        }
        return avgDelayTime;
    }