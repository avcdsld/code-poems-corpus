public static @CheckForNull Executor currentExecutor() {
        Thread t = Thread.currentThread();
        if (t instanceof Executor) return (Executor) t;
        return IMPERSONATION.get();
    }