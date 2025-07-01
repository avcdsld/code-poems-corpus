@Override AutoBuffer call(AutoBuffer ab) {
    ab._h2o.remove_task_tracking(ab.getTask());
    return ab;
  }