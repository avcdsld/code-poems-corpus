@Override
  public void recordTaskExecutionIdChange(String taskId, String executionId) {
    if (isHistoryLevelAtLeast(HistoryLevel.AUDIT)) {
      HistoricTaskInstanceEntity historicTaskInstance = getHistoricTaskInstanceEntityManager().findById(taskId);
      if (historicTaskInstance != null) {
        historicTaskInstance.setExecutionId(executionId);
      }
    }
  }