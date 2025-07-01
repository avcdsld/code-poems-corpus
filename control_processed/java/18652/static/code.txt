public Histogram getProbabilityHistogram(int labelClassIdx) {
        String title = "Network Probabilities Histogram - P(class " + labelClassIdx + ") - Data Labelled Class "
                        + labelClassIdx + " Only";
        int[] counts = probHistogramByLabelClass.getColumn(labelClassIdx).dup().data().asInt();
        return new Histogram(title, 0.0, 1.0, counts);
    }