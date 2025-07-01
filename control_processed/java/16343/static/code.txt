public static Map<String,Set<Writable>> getUniqueSequence(List<String> columnNames, Schema schema,
                                                               SequenceRecordReader sequenceData) {
        Map<String,Set<Writable>> m = new HashMap<>();
        for(String s : columnNames){
            m.put(s, new HashSet<>());
        }
        while(sequenceData.hasNext()){
            List<List<Writable>> next = sequenceData.sequenceRecord();
            for(List<Writable> step : next) {
                for (String s : columnNames) {
                    int idx = schema.getIndexOfColumn(s);
                    m.get(s).add(step.get(idx));
                }
            }
        }
        return m;
    }