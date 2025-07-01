public void initDataManagers() {
    if (attachmentDataManager == null) {
      attachmentDataManager = new MybatisAttachmentDataManager(this);
    }
    if (byteArrayDataManager == null) {
      byteArrayDataManager = new MybatisByteArrayDataManager(this);
    }
    if (commentDataManager == null) {
      commentDataManager = new MybatisCommentDataManager(this);
    }
    if (deploymentDataManager == null) {
      deploymentDataManager = new MybatisDeploymentDataManager(this);
    }
    if (eventLogEntryDataManager == null) {
      eventLogEntryDataManager = new MybatisEventLogEntryDataManager(this);
    }
    if (eventSubscriptionDataManager == null) {
      eventSubscriptionDataManager = new MybatisEventSubscriptionDataManager(this);
    }
    if (executionDataManager == null) {
      executionDataManager = new MybatisExecutionDataManager(this);
    }
    if (historicActivityInstanceDataManager == null) {
      historicActivityInstanceDataManager = new MybatisHistoricActivityInstanceDataManager(this);
    }
    if (historicDetailDataManager == null) {
      historicDetailDataManager = new MybatisHistoricDetailDataManager(this);
    }
    if (historicIdentityLinkDataManager == null) {
      historicIdentityLinkDataManager = new MybatisHistoricIdentityLinkDataManager(this);
    }
    if (historicProcessInstanceDataManager == null) {
      historicProcessInstanceDataManager = new MybatisHistoricProcessInstanceDataManager(this);
    }
    if (historicTaskInstanceDataManager == null) {
      historicTaskInstanceDataManager = new MybatisHistoricTaskInstanceDataManager(this);
    }
    if (historicVariableInstanceDataManager == null) {
      historicVariableInstanceDataManager = new MybatisHistoricVariableInstanceDataManager(this);
    }
    if (identityLinkDataManager == null) {
      identityLinkDataManager = new MybatisIdentityLinkDataManager(this);
    }
    if (jobDataManager == null) {
      jobDataManager = new MybatisJobDataManager(this);
    }
    if (timerJobDataManager == null) {
      timerJobDataManager = new MybatisTimerJobDataManager(this);
    }
    if (suspendedJobDataManager == null) {
      suspendedJobDataManager = new MybatisSuspendedJobDataManager(this);
    }
    if (deadLetterJobDataManager == null) {
      deadLetterJobDataManager = new MybatisDeadLetterJobDataManager(this);
    }
    if (modelDataManager == null) {
      modelDataManager = new MybatisModelDataManager(this);
    }
    if (processDefinitionDataManager == null) {
      processDefinitionDataManager = new MybatisProcessDefinitionDataManager(this);
    }
    if (processDefinitionInfoDataManager == null) {
      processDefinitionInfoDataManager = new MybatisProcessDefinitionInfoDataManager(this);
    }
    if (propertyDataManager == null) {
      propertyDataManager = new MybatisPropertyDataManager(this);
    }
    if (resourceDataManager == null) {
      resourceDataManager = new MybatisResourceDataManager(this);
    }
    if (taskDataManager == null) {
      taskDataManager = new MybatisTaskDataManager(this);
    }
    if (variableInstanceDataManager == null) {
      variableInstanceDataManager = new MybatisVariableInstanceDataManager(this);
    }
  }