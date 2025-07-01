public void retryLastFailedTask(String workflowId) {
        Preconditions.checkArgument(StringUtils.isNotBlank(workflowId), "workflow id cannot be blank");
        postForEntityWithUriVariablesOnly("workflow/{workflowId}/retry", workflowId);
    }