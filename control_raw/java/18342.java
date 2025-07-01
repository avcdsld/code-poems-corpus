public static void saveMapFileSequences(String path, JavaRDD<List<List<Writable>>> rdd, Configuration c,
                     Integer maxOutputFiles) {
        path = FilenameUtils.normalize(path, true);
        if (maxOutputFiles != null) {
            rdd = rdd.coalesce(maxOutputFiles);
        }
        JavaPairRDD<List<List<Writable>>, Long> dataIndexPairs = rdd.zipWithIndex();
        JavaPairRDD<LongWritable, SequenceRecordWritable> keyedByIndex =
                        dataIndexPairs.mapToPair(new SequenceRecordSavePrepPairFunction());

        keyedByIndex.saveAsNewAPIHadoopFile(path, LongWritable.class, SequenceRecordWritable.class,
                        MapFileOutputFormat.class, c);
    }