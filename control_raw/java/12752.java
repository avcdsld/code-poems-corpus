public static String getZone(String[] availZones, InstanceInfo myInfo) {
        String instanceZone = ((availZones == null || availZones.length == 0) ? "default"
                : availZones[0]);
        if (myInfo != null
                && myInfo.getDataCenterInfo().getName() == DataCenterInfo.Name.Amazon) {

            String awsInstanceZone = ((AmazonInfo) myInfo.getDataCenterInfo())
                    .get(AmazonInfo.MetaDataKey.availabilityZone);
            if (awsInstanceZone != null) {
                instanceZone = awsInstanceZone;
            }

        }
        return instanceZone;
    }