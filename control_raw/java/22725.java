public String createNoRetry(final String path, final byte[] data, final CreateMode mode) throws KeeperException,
                                                                                            InterruptedException {
        return zookeeper.create(path, data, acl, mode);
    }