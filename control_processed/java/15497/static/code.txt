public void unannounce(String path)
  {
    final ZKPaths.PathAndNode pathAndNode = ZKPaths.getPathAndNode(path);
    final String parentPath = pathAndNode.getPath();

    final ConcurrentMap<String, byte[]> subPaths = announcements.get(parentPath);

    if (subPaths == null || subPaths.remove(pathAndNode.getNode()) == null) {
      log.debug("Path[%s] not announced, cannot unannounce.", path);
      return;
    }
    log.info("unannouncing [%s]", path);

    try {
      curator.inTransaction().delete().forPath(path).and().commit();
    }
    catch (KeeperException.NoNodeException e) {
      log.info("node[%s] didn't exist anyway...", path);
    }
    catch (Exception e) {
      throw new RuntimeException(e);
    }
  }