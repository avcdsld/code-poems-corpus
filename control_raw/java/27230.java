public static CompletableFuture<Void> startAsync(Service service, Executor executor) {
        // Service.startAsync() will fail if the service is not in a NEW state. That is, if it is already RUNNING or
        // STARTED, then the method will fail synchronously, hence we are not in danger of not invoking our callbacks,
        // as long as we register the Listener before we attempt to start.
        // Nevertheless, do make a sanity check since once added, a Listener cannot be removed.
        Preconditions.checkState(service.state() == Service.State.NEW,
                "Service expected to be %s but was %s.", Service.State.NEW, service.state());
        Preconditions.checkNotNull(executor, "executor");
        CompletableFuture<Void> result = new CompletableFuture<>();
        service.addListener(new StartupListener(result), executor);
        service.startAsync();
        return result;
    }