public List<HistoricActivityInstance> executeList(CommandContext commandContext, Map<String, Object> parameterMap, int firstResult, int maxResults) {
    return commandContext.getHistoricActivityInstanceEntityManager().findHistoricActivityInstancesByNativeQuery(parameterMap, firstResult, maxResults);
  }