public void release(String pathInZooKeeper) throws Exception {
		final String path = normalizePath(pathInZooKeeper);

		try {
			client.delete().forPath(getLockPath(path));
		} catch (KeeperException.NoNodeException ignored) {
			// we have never locked this node
		} catch (Exception e) {
			throw new Exception("Could not release the lock: " + getLockPath(pathInZooKeeper) + '.', e);
		}
	}