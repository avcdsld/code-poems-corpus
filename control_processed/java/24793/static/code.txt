@Override
  public void run() {
    if (isTriggerExpired()) {
      logger.info(this + " expired");
      return;
    }

    final boolean isTriggerConditionMet = this.triggerCondition.isMet();
    if (isTriggerConditionMet) {
      logger.info("Condition " + this.triggerCondition.getExpression() + " met");
      for (final TriggerAction action : this.actions) {
        try {
          action.doAction();
        } catch (final Exception e) {
          logger.error("Failed to do action " + action.getDescription()
              + " for execution " + azkaban.execapp.Trigger.this.execId, e);
        }
      }
    }
  }