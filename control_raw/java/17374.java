public static double score(ComputationGraph model, MultiDataSetIterator testData, boolean average) {
        //TODO: do this properly taking into account division by N, L1/L2 etc
        double sumScore = 0.0;
        int totalExamples = 0;
        while (testData.hasNext()) {
            MultiDataSet ds = testData.next();
            long numExamples = ds.getFeatures(0).size(0);
            sumScore += numExamples * model.score(ds);
            totalExamples += numExamples;
        }

        if (!average)
            return sumScore;
        return sumScore / totalExamples;
    }