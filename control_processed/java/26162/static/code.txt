public Workflow getWorkflow(String workflowId, boolean includeTasks) {
        Preconditions.checkArgument(StringUtils.isNotBlank(workflowId), "workflow id cannot be blank");
        Workflow workflow = getForEntity("workflow/{workflowId}", new Object[]{"includeTasks", includeTasks}, Workflow.class, workflowId);
        populateWorkflowOutput(workflow);
        return workflow;
    }