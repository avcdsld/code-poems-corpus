public void setIsCoordinatingDiscoveryServer() {
        String instanceId = getId();
        if ((instanceId != null)
                && (instanceId.equals(ApplicationInfoManager.getInstance()
                .getInfo().getId()))) {
            isCoordinatingDiscoveryServer = Boolean.TRUE;
        } else {
            isCoordinatingDiscoveryServer = Boolean.FALSE;
        }
    }