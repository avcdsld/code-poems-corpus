public void updateWorkflowDefs(List<WorkflowDef> workflowDefs) {
        Preconditions.checkNotNull(workflowDefs, "Workflow defs list cannot be null");
        stub.updateWorkflows(
                MetadataServicePb.UpdateWorkflowsRequest.newBuilder()
                        .addAllDefs(
                                workflowDefs.stream().map(protoMapper::toProto)::iterator
                        )
                        .build()
        );
    }