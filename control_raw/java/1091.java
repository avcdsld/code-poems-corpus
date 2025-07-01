public void simplify()
    {
        if (sourceNode != null)
        {
            mdagDataArray = new SimpleMDAGNode[transitionCount];
            createSimpleMDAGTransitionSet(sourceNode, mdagDataArray, 0);
            simplifiedSourceNode = new SimpleMDAGNode('\0', false, sourceNode.getOutgoingTransitionCount());

            //Mark the previous MDAG data structure and equivalenceClassMDAGNodeHashMap
            //for garbage collection since they are no longer needed.
            sourceNode = null;
            equivalenceClassMDAGNodeHashMap = null;
            /////
        }
    }