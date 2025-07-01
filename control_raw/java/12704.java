public boolean isASGEnabled(InstanceInfo instanceInfo) {
        CacheKey cacheKey = new CacheKey(getAccountId(instanceInfo, accountId), instanceInfo.getASGName());
        Boolean result = asgCache.getIfPresent(cacheKey);
        if (result != null) {
            return result;
        } else {
            if (!serverConfig.shouldUseAwsAsgApi()) {
                // Disabled, cached values (if any) are still being returned if the caller makes
                // a decision to call the disabled client during some sort of transitioning
                // period, but no new values will be fetched while disabled.

                logger.info(("'{}' is not cached at the moment and won't be fetched because querying AWS ASGs "
                        + "has been disabled via the config, returning the fallback value."),
                            cacheKey);

                return true;
            }

            logger.info("Cache value for asg {} does not exist yet, async refreshing.", cacheKey.asgName);
            // Only do an async refresh if it does not yet exist. Do this to refrain from calling aws api too much
            asgCache.refresh(cacheKey);
            return true;
        }
    }