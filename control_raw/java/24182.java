protected void doRegister(String appName, String serviceName, ProviderInfo providerInfo) {

        registerAppInfoOnce(appName);

        if (LOGGER.isInfoEnabled(appName)) {
            LOGGER.infoWithApp(appName, LogCodes.getLog(LogCodes.INFO_ROUTE_REGISTRY_PUB, serviceName));
        }

        PublishServiceRequest publishServiceRequest = new PublishServiceRequest();
        publishServiceRequest.setServiceName(serviceName);
        ProviderMetaInfo providerMetaInfo = new ProviderMetaInfo();
        providerMetaInfo.setProtocol(providerInfo.getProtocolType());
        providerMetaInfo.setSerializeType(providerInfo.getSerializationType());
        providerMetaInfo.setAppName(appName);
        providerMetaInfo.setVersion(VERSION);
        publishServiceRequest.setProviderMetaInfo(providerMetaInfo);

        client.publishService(publishServiceRequest);
    }