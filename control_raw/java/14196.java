public ConfigurationMetadataRepository build() {
        val result = new SimpleConfigurationMetadataRepository();
        for (val repository : this.repositories) {
            result.include(repository);
        }
        return result;
    }