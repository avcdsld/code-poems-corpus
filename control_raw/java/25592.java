public final void setWork(final long work) {
    if (getWork() != WORK_UNKNOWN) {
      throw new IllegalStateException("Cannot set work amount if it was already previously specified");
    }
    new JAtomic() {
      @Override boolean abort(Job job) { return false; }
      @Override void update(Job old) { old._work = work; }
    }.apply(this);
  }