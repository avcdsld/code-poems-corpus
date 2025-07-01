protected void configureYahooClient(final Collection<BaseClient> properties) {
        val yahoo = pac4jProperties.getYahoo();
        if (StringUtils.isNotBlank(yahoo.getId()) && StringUtils.isNotBlank(yahoo.getSecret())) {
            val client = new YahooClient(yahoo.getId(), yahoo.getSecret());
            configureClient(client, yahoo);

            LOGGER.debug("Created client [{}] with identifier [{}]", client.getName(), client.getKey());
            properties.add(client);
        }
    }