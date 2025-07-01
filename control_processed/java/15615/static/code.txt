@Override
  public Node[] pickSeeds(List<Node> nodes)
  {
    int[] optimalIndices = new int[2];
    int numDims = nodes.get(0).getNumDims();

    double bestNormalized = 0.0;
    for (int i = 0; i < numDims; i++) {
      float minCoord = Float.POSITIVE_INFINITY;
      float maxCoord = Float.NEGATIVE_INFINITY;
      float lowestHighside = Float.POSITIVE_INFINITY;
      float highestLowSide = Float.NEGATIVE_INFINITY;
      int highestLowSideIndex = 0;
      int lowestHighSideIndex = 0;

      int counter = 0;
      for (Node node : nodes) {
        minCoord = Math.min(minCoord, node.getMinCoordinates()[i]);
        maxCoord = Math.max(maxCoord, node.getMaxCoordinates()[i]);

        if (node.getMinCoordinates()[i] > highestLowSide) {
          highestLowSide = node.getMinCoordinates()[i];
          highestLowSideIndex = counter;
        }
        if (node.getMaxCoordinates()[i] < lowestHighside) {
          lowestHighside = node.getMaxCoordinates()[i];
          lowestHighSideIndex = counter;
        }

        counter++;
      }
      double normalizedSeparation = (highestLowSideIndex == lowestHighSideIndex) ? -1.0 :
                                    Math.abs((highestLowSide - lowestHighside) / (maxCoord - minCoord));
      if (normalizedSeparation > bestNormalized) {
        optimalIndices[0] = highestLowSideIndex;
        optimalIndices[1] = lowestHighSideIndex;
        bestNormalized = normalizedSeparation;
      }
    }

    // Didn't actually find anything, just return first 2 children
    if (bestNormalized == 0) {
      optimalIndices[0] = 0;
      optimalIndices[1] = 1;
    }

    int indexToRemove1 = Math.min(optimalIndices[0], optimalIndices[1]);
    int indexToRemove2 = Math.max(optimalIndices[0], optimalIndices[1]);
    return new Node[]{nodes.remove(indexToRemove1), nodes.remove(indexToRemove2 - 1)};
  }