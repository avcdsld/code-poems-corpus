private static int findNodesToRelocate(final int[] array, final int maximumLength) {
        int currentNode = array.length - 2;
        for (int currentDepth = 1; currentDepth < maximumLength - 1 && currentNode > 1; currentDepth++) {
            currentNode =  first(array, currentNode - 1, 0);
        }
        return currentNode;
    }