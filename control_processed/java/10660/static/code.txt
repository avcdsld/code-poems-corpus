FinderPattern combineEstimate(float i, float j, float newModuleSize) {
    int combinedCount = count + 1;
    float combinedX = (count * getX() + j) / combinedCount;
    float combinedY = (count * getY() + i) / combinedCount;
    float combinedModuleSize = (count * estimatedModuleSize + newModuleSize) / combinedCount;
    return new FinderPattern(combinedX, combinedY, combinedModuleSize, combinedCount);
  }