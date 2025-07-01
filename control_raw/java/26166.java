public List<String> getRunningWorkflow(String workflowName, Integer version) {
        Preconditions.checkArgument(StringUtils.isNotBlank(workflowName), "Workflow name cannot be blank");
        return getForEntity("workflow/running/{name}", new Object[]{"version", version}, new GenericType<List<String>>() {
        }, workflowName);
    }