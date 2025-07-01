public Histogram getProbabilityHistogramAllClasses() {
        String title = "Network Probabilities Histogram - All Predictions and Classes";
        int[] counts = probHistogramOverall.data().asInt();
        return new Histogram(title, 0.0, 1.0, counts);
    }