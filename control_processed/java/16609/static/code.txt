public long numRecords() {
        if (numRecords == null) {
            try {
                numRecords = indexToKey.getNumRecords();
            } catch (IOException e) {
                throw new RuntimeException(e);
            }
        }
        return numRecords;
    }