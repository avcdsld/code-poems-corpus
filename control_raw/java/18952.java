public static JavaRDD<String> listPaths(JavaSparkContext sc, String path) throws IOException {
        return listPaths(sc, path, false);
    }