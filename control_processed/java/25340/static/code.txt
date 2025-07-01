static void tcp_call( final AutoBuffer ab ) {
    ab.getPort();
    long[] snap = ab.getA8();
    int idx = CLOUD.nidx(ab._h2o);
    if (idx >= 0 && idx < SNAPSHOT.length)
      SNAPSHOT[idx] = snap;     // Ignore out-of-cloud timelines
    ab.close();
    synchronized (TimeLine.class) {
      TimeLine.class.notify();
    }
  }