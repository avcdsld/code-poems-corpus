private ViterbiNode createGlueNode(int startIndex, ViterbiNode glueBase, String surface) {
        return new ViterbiNode(glueBase.getWordId(), surface, glueBase.getLeftId(), glueBase.getRightId(),
                        glueBase.getWordCost(), startIndex, ViterbiNode.Type.INSERTED);
    }