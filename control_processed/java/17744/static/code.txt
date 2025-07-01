public static <T> T readObjectFromFile(String path, Class<T> type, JavaSparkContext sc) throws IOException {
        return readObjectFromFile(path, type, sc.sc());
    }