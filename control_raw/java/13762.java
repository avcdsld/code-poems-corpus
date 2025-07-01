public File getStandaloneProfileConfigurationDirectory() {
        val file = environment.getProperty("cas.standalone.configurationDirectory", File.class);
        if (file != null && file.exists()) {
            LOGGER.trace("Received standalone configuration directory [{}]", file);
            return file;
        }

        return Arrays.stream(DEFAULT_CAS_CONFIG_DIRECTORIES)
            .filter(File::exists)
            .findFirst()
            .orElse(null);
    }