public void resumeWorkflow(String workflowId) {
        Preconditions.checkArgument(StringUtils.isNotBlank(workflowId), "workflow id cannot be blank");
        stub.resumeWorkflow(WorkflowServicePb.ResumeWorkflowRequest.newBuilder()
                .setWorkflowId(workflowId)
                .build()
        );
    }