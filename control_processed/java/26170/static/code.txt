public String rerunWorkflow(String workflowId, RerunWorkflowRequest rerunWorkflowRequest) {
        Preconditions.checkArgument(StringUtils.isNotBlank(workflowId), "workflow id cannot be blank");
        Preconditions.checkNotNull(rerunWorkflowRequest, "RerunWorkflowRequest cannot be null");

        return postForEntity("workflow/{workflowId}/rerun", rerunWorkflowRequest, null, String.class, workflowId);
    }