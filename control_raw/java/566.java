public void decrementTargetIncomingTransitionCounts()
    {
        for(Entry<Character, MDAGNode> transitionKeyValuePair: outgoingTransitionTreeMap.entrySet())
            transitionKeyValuePair.getValue().incomingTransitionCount--;
    }