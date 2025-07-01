private TimerTask getASGUpdateTask() {
        return new TimerTask() {

            @Override
            public void run() {
                try {
                    if (!serverConfig.shouldUseAwsAsgApi()) {
                        // Disabled via the config, no-op.
                        return;
                    }

                    // First get the active ASG names
                    Set<CacheKey> cacheKeys = getCacheKeys();
                    if (logger.isDebugEnabled()) {
                        logger.debug("Trying to  refresh the keys for {}", Arrays.toString(cacheKeys.toArray()));
                    }
                    for (CacheKey key : cacheKeys) {
                        try {
                            asgCache.refresh(key);
                        } catch (Throwable e) {
                            logger.error("Error updating the ASG cache for {}", key, e);
                        }

                    }

                } catch (Throwable e) {
                    logger.error("Error updating the ASG cache", e);
                }

            }

        };
    }