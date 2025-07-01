public static Config fromYAML(Reader reader) throws IOException {
        ConfigSupport support = new ConfigSupport();
        return support.fromYAML(reader, Config.class);
    }