protected List<mxPoint> optimizeEdgePoints(List<mxPoint> unoptimizedPointsList) {
    List<mxPoint> optimizedPointsList = new ArrayList<mxPoint>();
    for (int i = 0; i < unoptimizedPointsList.size(); i++) {

      boolean keepPoint = true;
      mxPoint currentPoint = unoptimizedPointsList.get(i);

      // When three points are on the same x-axis with same y value, the
      // middle point can be removed
      if (i > 0 && i != unoptimizedPointsList.size() - 1) {

        mxPoint previousPoint = unoptimizedPointsList.get(i - 1);
        mxPoint nextPoint = unoptimizedPointsList.get(i + 1);

        if (currentPoint.getX() >= previousPoint.getX() && currentPoint.getX() <= nextPoint.getX() && currentPoint.getY() == previousPoint.getY() && currentPoint.getY() == nextPoint.getY()) {
          keepPoint = false;
        } else if (currentPoint.getY() >= previousPoint.getY() && currentPoint.getY() <= nextPoint.getY() && currentPoint.getX() == previousPoint.getX() && currentPoint.getX() == nextPoint.getX()) {
          keepPoint = false;
        }

      }

      if (keepPoint) {
        optimizedPointsList.add(currentPoint);
      }

    }

    return optimizedPointsList;
  }