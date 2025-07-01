public void shuffleAndIndexInstances(Map<String, Applications> remoteRegionsRegistry,
            EurekaClientConfig clientConfig, InstanceRegionChecker instanceRegionChecker) {
        shuffleInstances(clientConfig.shouldFilterOnlyUpInstances(), true, remoteRegionsRegistry, clientConfig,
                instanceRegionChecker);
    }