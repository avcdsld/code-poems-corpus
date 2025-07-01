@Override
    public void attachThreadToDevice(long threadId, Integer deviceId) {
        val t = Thread.currentThread();
        String name = "N/A";
        if (t.getId() == threadId)
            name = t.getName();

        List<Integer> devices = new ArrayList<>(CudaEnvironment.getInstance().getConfiguration().getAvailableDevices());
        logger.trace("Manually mapping thread [{} - {}] to device [{}], out of [{}] devices...", threadId,
                name, deviceId, devices.size());
        affinityMap.put(threadId, deviceId);
    }