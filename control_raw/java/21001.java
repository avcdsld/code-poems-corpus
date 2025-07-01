@Override
    public Future<?> submit(Runnable task) {
        return schedule(task, getDefaultDelayForTask(), TimeUnit.MILLISECONDS);
    }