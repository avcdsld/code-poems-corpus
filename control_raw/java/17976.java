public DataSet loadFromMetaData(List<RecordMetaData> list) throws IOException {
        if (underlying == null) {
            SequenceRecord r = recordReader.loadSequenceFromMetaData(list.get(0));
            initializeUnderlying(r);
        }

        //Two cases: single vs. multiple reader...
        List<RecordMetaData> l = new ArrayList<>(list.size());
        if (singleSequenceReaderMode) {
            for (RecordMetaData m : list) {
                l.add(new RecordMetaDataComposableMap(Collections.singletonMap(READER_KEY, m)));
            }
        } else {
            for (RecordMetaData m : list) {
                RecordMetaDataComposable rmdc = (RecordMetaDataComposable) m;
                Map<String, RecordMetaData> map = new HashMap<>(2);
                map.put(READER_KEY, rmdc.getMeta()[0]);
                map.put(READER_KEY_LABEL, rmdc.getMeta()[1]);
                l.add(new RecordMetaDataComposableMap(map));
            }
        }

        return mdsToDataSet(underlying.loadFromMetaData(l));
    }