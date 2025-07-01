protected void callActivityEndListeners(DelegateExecution execution) {
    Context.getCommandContext().getProcessEngineConfiguration().getListenerNotificationHelper()
      .executeExecutionListeners(activity, execution, ExecutionListener.EVENTNAME_END);
  }