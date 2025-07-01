protected void configureWordPressClient(final Collection<BaseClient> properties) {
        val wp = pac4jProperties.getWordpress();
        if (StringUtils.isNotBlank(wp.getId()) && StringUtils.isNotBlank(wp.getSecret())) {
            val client = new WordPressClient(wp.getId(), wp.getSecret());
            configureClient(client, wp);

            LOGGER.debug("Created client [{}] with identifier [{}]", client.getName(), client.getKey());
            properties.add(client);
        }
    }