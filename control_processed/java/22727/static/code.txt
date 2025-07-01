public <T> T retryOperation(ZooKeeperOperation<T> operation) throws KeeperException, InterruptedException {
        if (!running.get()) {
            throw new ArbitrateException("Zookeeper is destory ,should never be used ....");
        }

        KeeperException exception = null;
        for (int i = 0; i < maxRetry; i++) {
            int version = cversion.get(); // 获取版本
            int retryCount = i + 1;
            try {
                if (!zookeeper.getState().isAlive()) {
                    retryDelay(retryCount);
                    cleanup(version);
                } else {
                    return (T) operation.execute();
                }
            } catch (KeeperException.SessionExpiredException e) {
                logger.warn("Session expired for: " + this + " so reconnecting " + (i + 1) + " times due to: " + e, e);
                retryDelay(retryCount);
                cleanup(version);
            } catch (KeeperException.ConnectionLossException e) { // 特殊处理Connection Loss
                if (exception == null) {
                    exception = e;
                }
                logger.warn("Attempt " + retryCount + " failed with connection loss so " + "attempting to reconnect: "
                            + e, e);
                retryDelay(retryCount);
            }
        }

        throw exception;
    }