public static List<DataMediaPair> findDataMediaPairByMediaId(Pipeline pipeline, Long tid) {
        Assert.notNull(pipeline);
        List<DataMediaPair> pairs = new ArrayList<DataMediaPair>();
        for (DataMediaPair pair : pipeline.getPairs()) {
            if (pair.getSource().getId().equals(tid)) {
                pairs.add(pair);
            } else if (pair.getTarget().getId().equals(tid)) {
                pairs.add(pair);
            }
        }

        return pairs;
    }