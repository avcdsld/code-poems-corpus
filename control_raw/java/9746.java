public static Map<String, ? extends CacheConfig> fromJSON(File file) throws IOException {
        return new CacheConfigSupport().fromJSON(file);
    }