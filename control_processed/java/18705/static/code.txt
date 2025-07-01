public SDVariable huberLoss(String name, @NonNull SDVariable label, @NonNull SDVariable predictions, double delta) {
        return huberLoss(name, label, predictions, null, LossReduce.MEAN_BY_NONZERO_WEIGHT_COUNT, delta);
    }