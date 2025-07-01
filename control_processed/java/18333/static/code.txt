public static void saveSequenceFile(String path, JavaRDD<List<Writable>> rdd,  Integer maxOutputFiles) {
        path = FilenameUtils.normalize(path, true);
        if (maxOutputFiles != null) {
            rdd = rdd.coalesce(maxOutputFiles);
        }
        JavaPairRDD<List<Writable>, Long> dataIndexPairs = rdd.zipWithUniqueId(); //Note: Long values are unique + NOT contiguous; more efficient than zipWithIndex
        JavaPairRDD<LongWritable, RecordWritable> keyedByIndex =
                        dataIndexPairs.mapToPair(new RecordSavePrepPairFunction());

        keyedByIndex.saveAsNewAPIHadoopFile(path, LongWritable.class, RecordWritable.class,
                        SequenceFileOutputFormat.class);
    }