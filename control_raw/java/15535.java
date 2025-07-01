private boolean possiblySuspendOrResumeSupervisorInternal(String id, boolean suspend)
  {
    Pair<Supervisor, SupervisorSpec> pair = supervisors.get(id);
    if (pair == null || pair.rhs.isSuspended() == suspend) {
      return false;
    }

    SupervisorSpec nextState = suspend ? pair.rhs.createSuspendedSpec() : pair.rhs.createRunningSpec();
    possiblyStopAndRemoveSupervisorInternal(nextState.getId(), false);
    return createAndStartSupervisorInternal(nextState, true);
  }