protected HttpClient getHttpClient() {
        HttpClient client = new HttpClient();
        if (Jenkins.getInstance() != null) {
            ProxyConfiguration proxy = Jenkins.getInstance().proxy;
            if (useProxy && (proxy != null)){
                client.getHostConfiguration().setProxy(proxy.name, proxy.port);
                String username = proxy.getUserName();
                String password = proxy.getPassword();
                if (!StringUtils.isEmpty(username.trim()) && !StringUtils.isEmpty(password.trim())) {
                    logger.info("Using proxy authentication (user=" + username + ")");
                    client.getState().setProxyCredentials(AuthScope.ANY,
                            new UsernamePasswordCredentials(username.trim(), password.trim()));
                }
            }
        }
        return client;
    }