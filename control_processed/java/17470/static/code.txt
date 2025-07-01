public INDArray scoreExamples(DataSet data, boolean addRegularizationTerms) {
        try{
            return scoreExamplesHelper(data, addRegularizationTerms);
        } catch (OutOfMemoryError e){
            CrashReportingUtil.writeMemoryCrashDump(this, e);
            throw e;
        }
    }