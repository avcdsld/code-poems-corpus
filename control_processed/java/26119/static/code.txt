public String updateWorkflow(Workflow workflow) {
        executionDAO.updateWorkflow(workflow);
        indexDAO.indexWorkflow(workflow);
        return workflow.getWorkflowId();
    }