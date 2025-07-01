@Deprecated
    public void cliDisconnect(String cause) throws ExecutionException, InterruptedException {
        checkPermission(DISCONNECT);
        disconnect(new ByCLI(cause)).get();
    }