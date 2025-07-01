private static boolean isAcceptNode(Object nodeObj)
    {
        if (nodeObj != null)
        {
            Class nodeObjClass = nodeObj.getClass();

            if (nodeObjClass.equals(MDAGNode.class))
                return ((MDAGNode) nodeObj).isAcceptNode();
            else if (nodeObjClass.equals(SimpleMDAGNode.class))
                return ((SimpleMDAGNode) nodeObj).isAcceptNode();

        }

        throw new IllegalArgumentException("Argument is not an MDAGNode or SimpleMDAGNode");
    }