public Applications getApplicationDeltasFromMultipleRegions(String[] remoteRegions) {
        if (null == remoteRegions) {
            remoteRegions = allKnownRemoteRegions; // null means all remote regions.
        }

        boolean includeRemoteRegion = remoteRegions.length != 0;

        if (includeRemoteRegion) {
            GET_ALL_WITH_REMOTE_REGIONS_CACHE_MISS_DELTA.increment();
        } else {
            GET_ALL_CACHE_MISS_DELTA.increment();
        }

        Applications apps = new Applications();
        apps.setVersion(responseCache.getVersionDeltaWithRegions().get());
        Map<String, Application> applicationInstancesMap = new HashMap<String, Application>();
        try {
            write.lock();
            Iterator<RecentlyChangedItem> iter = this.recentlyChangedQueue.iterator();
            logger.debug("The number of elements in the delta queue is :{}", this.recentlyChangedQueue.size());
            while (iter.hasNext()) {
                Lease<InstanceInfo> lease = iter.next().getLeaseInfo();
                InstanceInfo instanceInfo = lease.getHolder();
                logger.debug("The instance id {} is found with status {} and actiontype {}",
                        instanceInfo.getId(), instanceInfo.getStatus().name(), instanceInfo.getActionType().name());
                Application app = applicationInstancesMap.get(instanceInfo.getAppName());
                if (app == null) {
                    app = new Application(instanceInfo.getAppName());
                    applicationInstancesMap.put(instanceInfo.getAppName(), app);
                    apps.addApplication(app);
                }
                app.addInstance(new InstanceInfo(decorateInstanceInfo(lease)));
            }

            if (includeRemoteRegion) {
                for (String remoteRegion : remoteRegions) {
                    RemoteRegionRegistry remoteRegistry = regionNameVSRemoteRegistry.get(remoteRegion);
                    if (null != remoteRegistry) {
                        Applications remoteAppsDelta = remoteRegistry.getApplicationDeltas();
                        if (null != remoteAppsDelta) {
                            for (Application application : remoteAppsDelta.getRegisteredApplications()) {
                                if (shouldFetchFromRemoteRegistry(application.getName(), remoteRegion)) {
                                    Application appInstanceTillNow =
                                            apps.getRegisteredApplications(application.getName());
                                    if (appInstanceTillNow == null) {
                                        appInstanceTillNow = new Application(application.getName());
                                        apps.addApplication(appInstanceTillNow);
                                    }
                                    for (InstanceInfo instanceInfo : application.getInstances()) {
                                        appInstanceTillNow.addInstance(new InstanceInfo(instanceInfo));
                                    }
                                }
                            }
                        }
                    }
                }
            }

            Applications allApps = getApplicationsFromMultipleRegions(remoteRegions);
            apps.setAppsHashCode(allApps.getReconcileHashCode());
            return apps;
        } finally {
            write.unlock();
        }
    }