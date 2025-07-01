public void fit(@NonNull MultiDataSetIterator iterator) {
        List<S.Builder> featureNormBuilders = new ArrayList<>();
        List<S.Builder> labelNormBuilders = new ArrayList<>();

        iterator.reset();
        while (iterator.hasNext()) {
            MultiDataSet next = iterator.next();
            fitPartial(next, featureNormBuilders, labelNormBuilders);
        }

        featureStats = buildList(featureNormBuilders);
        if (isFitLabel()) {
            labelStats = buildList(labelNormBuilders);
        }
    }