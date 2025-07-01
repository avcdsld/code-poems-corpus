public void addInvolvedExecution(ExecutionEntity executionEntity) {
        if (executionEntity.getId() != null) {
            involvedExecutions.put(executionEntity.getId(),
                                   executionEntity);
        }
    }