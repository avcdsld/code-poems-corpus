protected void purgeDeviceObject(Long threadId, Integer deviceId, Long objectId, AllocationPoint point,
                    boolean copyback) {
        memoryHandler.purgeDeviceObject(threadId, deviceId, objectId, point, copyback);

        // since we can't allow java object without native memory, we explicitly specify that memory is handled using HOST memory only, after device memory is released
        //point.setAllocationStatus(AllocationStatus.HOST);

        //memoryHandler.purgeZeroObject(point.getBucketId(), point.getObjectId(), point, copyback);
    }