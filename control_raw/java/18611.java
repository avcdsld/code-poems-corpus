public static void exportStringLocal(File outputFile, JavaRDD<String> data, int rngSeed) throws Exception {
        List<String> linesList = data.collect(); //Requires all data in memory
        if (!(linesList instanceof ArrayList))
            linesList = new ArrayList<>(linesList);
        Collections.shuffle(linesList, new Random(rngSeed));

        FileUtils.writeLines(outputFile, linesList);
    }