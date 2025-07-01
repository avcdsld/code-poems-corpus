@Override
  public void setupLocal() {
    super.setupLocal();
    _res = new DeepLearningTask(_jobKey, _sharedmodel, _sync_fraction, _iteration, this);
    addToPendingCount(1);
    _res.dfork(null, _fr, true /*run_local*/);
  }