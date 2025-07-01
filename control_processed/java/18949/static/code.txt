public static <T> JavaRDD<T>[] balancedRandomSplit(int totalObjectCount, int numObjectsPerSplit, JavaRDD<T> data,
                    long rngSeed) {
        JavaRDD<T>[] splits;
        if (totalObjectCount <= numObjectsPerSplit) {
            splits = (JavaRDD<T>[]) Array.newInstance(JavaRDD.class, 1);
            splits[0] = data;
        } else {
            int numSplits = totalObjectCount / numObjectsPerSplit; //Intentional round down
            splits = (JavaRDD<T>[]) Array.newInstance(JavaRDD.class, numSplits);
            for (int i = 0; i < numSplits; i++) {
                splits[i] = data.mapPartitionsWithIndex(new SplitPartitionsFunction<T>(i, numSplits, rngSeed), true);
            }

        }
        return splits;
    }