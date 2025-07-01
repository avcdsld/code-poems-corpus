public static DataQualityAnalysis analyzeQualitySequence(Schema schema, SequenceRecordReader data) {
        int nColumns = schema.numColumns();
        List<QualityAnalysisState> states = new ArrayList<>();
        QualityAnalysisAddFunction addFn = new QualityAnalysisAddFunction(schema);
        while(data.hasNext()){
            List<List<Writable>> seq = data.sequenceRecord();
            for(List<Writable> step : seq){
                states = addFn.apply(states, step);
            }
        }

        List<ColumnQuality> list = new ArrayList<>(nColumns);

        for (QualityAnalysisState qualityState : states) {
            list.add(qualityState.getColumnQuality());
        }
        return new DataQualityAnalysis(schema, list);
    }