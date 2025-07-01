@Override
    public void free(AllocationPoint point, AllocationStatus target) {
        //if (point.getAllocationStatus() == AllocationStatus.DEVICE)
        //deviceAllocations.get(point.getDeviceId()).remove(point.getObjectId());

        //zeroAllocations.get(point.getBucketId()).remove(point.getObjectId());
        if (point.getAllocationStatus() == AllocationStatus.DEVICE)
            deviceMemoryTracker.subFromAllocation(Thread.currentThread().getId(), point.getDeviceId(),
                            AllocationUtils.getRequiredMemory(point.getShape()));

        memoryProvider.free(point);
    }