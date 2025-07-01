public synchronized void start() {
        if (monitorActive) {
            return;
        }
        lastTime.set(milliSecondFromNano());
        long localCheckInterval = checkInterval.get();
        // if executor is null, it means it is piloted by a GlobalChannelTrafficCounter, so no executor
        if (localCheckInterval > 0 && executor != null) {
            monitorActive = true;
            monitor = new TrafficMonitoringTask();
            scheduledFuture =
                executor.schedule(monitor, localCheckInterval, TimeUnit.MILLISECONDS);
        }
    }