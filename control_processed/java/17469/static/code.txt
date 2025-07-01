public INDArray scoreExamples(DataSetIterator iter, boolean addRegularizationTerms) {
        List<INDArray> out = new ArrayList<>();

        while (iter.hasNext()) {
            out.add(scoreExamples(iter.next(), addRegularizationTerms));
        }
        return Nd4j.toFlattened('f', out);
    }