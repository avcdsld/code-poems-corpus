public synchronized void setExecutors(ExecutorService svc) {
        ExecutorService old = this.executors;
        this.executors = svc;
        // gradually executions will be taken over by a new pool
        old.shutdown();
    }