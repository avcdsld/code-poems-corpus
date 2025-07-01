@Override
    public DataBuffer replicateToDevice(Integer deviceId, DataBuffer buffer) {
        if (buffer == null)
            return null;

        int currentDeviceId = AtomicAllocator.getInstance().getDeviceId();
        if (currentDeviceId != deviceId) {
            Nd4j.getMemoryManager().releaseCurrentContext();
            NativeOpsHolder.getInstance().getDeviceNativeOps().setDevice(deviceId);
            Nd4j.getAffinityManager().attachThreadToDevice(Thread.currentThread().getId(), deviceId);
        }

        DataBuffer dstBuffer = Nd4j.createBuffer(buffer.dataType(), buffer.length(), false);
        AtomicAllocator.getInstance().memcpy(dstBuffer, buffer);

        if (currentDeviceId != deviceId) {
            Nd4j.getMemoryManager().releaseCurrentContext();
            NativeOpsHolder.getInstance().getDeviceNativeOps().setDevice(currentDeviceId);
            Nd4j.getAffinityManager().attachThreadToDevice(Thread.currentThread().getId(), currentDeviceId);
        }

        return dstBuffer;
    }