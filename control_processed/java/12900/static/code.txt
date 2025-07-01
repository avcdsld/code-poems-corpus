@Override
  public void recordTaskNameChange(String taskId, String taskName) {
    if (isHistoryLevelAtLeast(HistoryLevel.AUDIT)) {
      HistoricTaskInstanceEntity historicTaskInstance = getHistoricTaskInstanceEntityManager().findById(taskId);
      if (historicTaskInstance != null) {
        historicTaskInstance.setName(taskName);
      }
    }
  }