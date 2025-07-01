public void recoverIncompleteTriggerInstances() {
    final Collection<TriggerInstance> unfinishedTriggerInstances = this.flowTriggerInstanceLoader
        .getIncompleteTriggerInstances();
    for (final TriggerInstance triggerInstance : unfinishedTriggerInstances) {
      if (triggerInstance.getFlowTrigger() != null) {
        recoverTriggerInstance(triggerInstance);
      } else {
        logger.error("cannot recover the trigger instance {}, flow trigger is null,"
            + " cancelling it ", triggerInstance.getId());

        //finalize unrecoverable trigger instances
        // the following situation would cause trigger instances unrecoverable:
        // 1. project A with flow A associated with flow trigger A is uploaded
        // 2. flow trigger A starts to run
        // 3. project A with flow B without any flow trigger is uploaded
        // 4. web server restarts
        // in this case, flow trigger instance of flow trigger A will be equipped with latest
        // project, thus failing to find the flow trigger since new project doesn't contain flow
        // trigger at all
        if (isDoneButFlowNotExecuted(triggerInstance)) {
          triggerInstance.setFlowExecId(Constants.FAILED_EXEC_ID);
          this.flowTriggerInstanceLoader.updateAssociatedFlowExecId(triggerInstance);
        } else {
          for (final DependencyInstance depInst : triggerInstance.getDepInstances()) {
            if (!Status.isDone(depInst.getStatus())) {
              processStatusAndCancelCauseUpdate(depInst, Status.CANCELLED,
                  CancellationCause.FAILURE);
              this.triggerProcessor.processTermination(depInst.getTriggerInstance());
            }
          }
        }
      }
    }
  }