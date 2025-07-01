public static void helpQuiesce() {
        ForkJoinWorkerThread wt =
            (ForkJoinWorkerThread)Thread.currentThread();
        wt.pool.helpQuiescePool(wt.workQueue);
    }