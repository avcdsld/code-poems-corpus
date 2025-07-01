function getRangePath(points, smooth, isInCircle, cfg) {
  var topPoints = [];
  var isStack = cfg.isStack;
  var bottomPoints = [];
  for (var i = 0; i < points.length; i++) {
    var point = points[i];
    var tmp = ShapeUtil.splitPoints(point);
    bottomPoints.push(tmp[0]);
    topPoints.push(tmp[1]);
  }
  var topPath = getSinglePath(topPoints, smooth, isInCircle, cfg);
  var bottomPath = getSinglePath(bottomPoints, smooth, isInCircle, cfg);
  if (isStack) {
    return topPath;
  }
  return topPath.concat(bottomPath);
}