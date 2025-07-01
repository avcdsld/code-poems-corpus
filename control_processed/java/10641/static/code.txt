public ResultPoint[] detect() throws NotFoundException {
    int height = image.getHeight();
    int width = image.getWidth();
    int halfHeight = height / 2;
    int halfWidth = width / 2;
    int deltaY = Math.max(1, height / (MAX_MODULES * 8));
    int deltaX = Math.max(1, width / (MAX_MODULES * 8));

    int top = 0;
    int bottom = height;
    int left = 0;
    int right = width;
    ResultPoint pointA = findCornerFromCenter(halfWidth, 0, left, right,
        halfHeight, -deltaY, top, bottom, halfWidth / 2);
    top = (int) pointA.getY() - 1;
    ResultPoint pointB = findCornerFromCenter(halfWidth, -deltaX, left, right,
        halfHeight, 0, top, bottom, halfHeight / 2);
    left = (int) pointB.getX() - 1;
    ResultPoint pointC = findCornerFromCenter(halfWidth, deltaX, left, right,
        halfHeight, 0, top, bottom, halfHeight / 2);
    right = (int) pointC.getX() + 1;
    ResultPoint pointD = findCornerFromCenter(halfWidth, 0, left, right,
        halfHeight, deltaY, top, bottom, halfWidth / 2);
    bottom = (int) pointD.getY() + 1;

    // Go try to find point A again with better information -- might have been off at first.
    pointA = findCornerFromCenter(halfWidth, 0, left, right,
        halfHeight, -deltaY, top, bottom, halfWidth / 4);

    return new ResultPoint[] { pointA, pointB, pointC, pointD };
  }