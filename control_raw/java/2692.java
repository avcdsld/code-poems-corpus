@Override
  public synchronized void init(HiveConf hiveConf) {
    ensureCurrentState(STATE.NOTINITED);
    this.hiveConf = hiveConf;
    changeState(STATE.INITED);
    LOG.info("Service:" + getName() + " is inited.");
  }