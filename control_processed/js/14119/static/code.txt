function isLineRightOfPoint(point, lp1, lp2) {
  // If both right of point return true
  if (lp1.x > point.x && lp2.x > point.x) {
    return true;
  }

  // Catch when line is vertical.
  if (lp1.x === lp2.x) {
    return point.x < lp1.x;
  }

  // Put leftmost point in lp1
  if (lp1.x > lp2.x) {
    const lptemp = lp1;

    lp1 = lp2;
    lp2 = lptemp;
  }
  const lPointY = lineSegmentAtPoint(point, lp1, lp2);

  // If the lp1.x and lp2.x enclose point.x check gradient of line and see if
  // Point is above or below the line to calculate if it inside.
  if (Math.sign(lPointY.gradient) * point.y > lPointY.value) {
    return true;
  }

  return false;
}