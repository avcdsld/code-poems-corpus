public static boolean isReachable(String processDefinitionId, String sourceElementId, String targetElementId) {

    // Fetch source and target elements
    Process process = ProcessDefinitionUtil.getProcess(processDefinitionId);

    FlowElement sourceFlowElement = process.getFlowElement(sourceElementId, true);
    FlowNode sourceElement = null;
    if (sourceFlowElement instanceof FlowNode) {
      sourceElement = (FlowNode) sourceFlowElement;
    } else if (sourceFlowElement instanceof SequenceFlow) {
      sourceElement = (FlowNode) ((SequenceFlow) sourceFlowElement).getTargetFlowElement();
    }

    FlowElement targetFlowElement = process.getFlowElement(targetElementId, true);
    FlowNode targetElement = null;
    if (targetFlowElement instanceof FlowNode) {
      targetElement = (FlowNode) targetFlowElement;
    } else if (targetFlowElement instanceof SequenceFlow) {
      targetElement = (FlowNode) ((SequenceFlow) targetFlowElement).getTargetFlowElement();
    }

    if (sourceElement == null) {
      throw new ActivitiException("Invalid sourceElementId '" + sourceElementId + "': no element found for this id n process definition '" + processDefinitionId + "'");
    }
    if (targetElement == null) {
      throw new ActivitiException("Invalid targetElementId '" + targetElementId + "': no element found for this id n process definition '" + processDefinitionId + "'");
    }

    Set<String> visitedElements = new HashSet<String>();
    return isReachable(process, sourceElement, targetElement, visitedElements);
  }