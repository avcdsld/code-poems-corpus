@Override
    @Synchronized
    public void registerHost(Host host) {
        Preconditions.checkNotNull(host, "host");
        Exceptions.checkArgument(!entryMap.containsKey(host), "host", "host is already registered to cluster.");

        String hostPath = ZKPaths.makePath(getPathPrefix(), host.toString());
        PersistentNode node = new PersistentNode(client, CreateMode.EPHEMERAL, false, hostPath,
                host.toBytes());

        node.start(); //start creation of ephemeral node in background.
        entryMap.put(host, node);
    }