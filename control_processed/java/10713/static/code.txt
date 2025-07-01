private ResultPoint[] detectSolid2(ResultPoint[] points) {
    // A..D
    // :  :
    // B--C
    ResultPoint pointA = points[0];
    ResultPoint pointB = points[1];
    ResultPoint pointC = points[2];
    ResultPoint pointD = points[3];

    // Transition detection on the edge is not stable.
    // To safely detect, shift the points to the module center.
    int tr = transitionsBetween(pointA, pointD);
    ResultPoint pointBs = shiftPoint(pointB, pointC, (tr + 1) * 4);
    ResultPoint pointCs = shiftPoint(pointC, pointB, (tr + 1) * 4);
    int trBA = transitionsBetween(pointBs, pointA);
    int trCD = transitionsBetween(pointCs, pointD);

    // 0..3
    // |  :
    // 1--2
    if (trBA < trCD) {
      // solid sides: A-B-C
      points[0] = pointA;
      points[1] = pointB;
      points[2] = pointC;
      points[3] = pointD;
    } else {
      // solid sides: B-C-D
      points[0] = pointB;
      points[1] = pointC;
      points[2] = pointD;
      points[3] = pointA;
    }

    return points;
  }