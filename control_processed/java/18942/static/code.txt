public static void writeStringToFile(String path, String toWrite, SparkContext sc) throws IOException {
        FileSystem fileSystem = FileSystem.get(sc.hadoopConfiguration());
        try (BufferedOutputStream bos = new BufferedOutputStream(fileSystem.create(new Path(path)))) {
            bos.write(toWrite.getBytes("UTF-8"));
        }
    }