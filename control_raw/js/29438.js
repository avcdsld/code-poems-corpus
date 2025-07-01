function getPath(cfg, smooth) {
  var path = void 0;
  var points = cfg.points;
  var isInCircle = cfg.isInCircle;
  var first = points[0];
  if (Util.isArray(first.y)) {
    path = getRangePath(points, smooth, isInCircle, cfg);
  } else {
    path = getSinglePath(points, smooth, isInCircle, cfg);
  }
  return path;
}