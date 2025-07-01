public RemoteProxy remove(RemoteProxy proxy) {
    // Find the original proxy. While the supplied one is logically equivalent, it may be a fresh object with
    // an empty TestSlot list, which doesn't figure into the proxy equivalence check.  Since we want to free up
    // those test sessions, we need to operate on that original object.
    for (RemoteProxy p : proxies) {
      if (p.equals(proxy)) {
        proxies.remove(p);
        return p;
      }
    }
    throw new IllegalStateException("Did not contain proxy" + proxy);
  }