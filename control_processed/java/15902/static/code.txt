public <T> T addMaybeStartStartCloseInstance(T o) throws Exception
  {
    addMaybeStartHandler(new StartCloseHandler(o));
    return o;
  }