public static JavaRDD<DataSet> shuffleExamples(JavaRDD<DataSet> rdd, int newBatchSize, int numPartitions) {
        //Step 1: split into individual examples, mapping to a pair RDD (random key in range 0 to numPartitions)

        JavaPairRDD<Integer, DataSet> singleExampleDataSets =
                        rdd.flatMapToPair(new SplitDataSetExamplesPairFlatMapFunction(numPartitions));

        //Step 2: repartition according to the random keys
        singleExampleDataSets = singleExampleDataSets.partitionBy(new HashPartitioner(numPartitions));

        //Step 3: Recombine
        return singleExampleDataSets.values().mapPartitions(new BatchDataSetsFunction(newBatchSize));
    }