public static String getExtractStage(Long pipelineId, Long processId) {
        return getProcess(pipelineId, processId) + "/" + ArbitrateConstants.NODE_EXTRACTED;
    }