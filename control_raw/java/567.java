public void reassignOutgoingTransition(char letter, MDAGNode oldTargetNode, MDAGNode newTargetNode)
    {
        oldTargetNode.incomingTransitionCount--;
        newTargetNode.incomingTransitionCount++;
        
        outgoingTransitionTreeMap.put(letter, newTargetNode);
    }