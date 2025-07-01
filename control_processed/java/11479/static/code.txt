public static void touch(@Nonnull File file) throws IOException {
        Files.newOutputStream(fileToPath(file)).close();
    }