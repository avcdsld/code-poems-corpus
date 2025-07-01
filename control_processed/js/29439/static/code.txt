function _getInterPath(points) {
  var path = [];
  Util.each(points, function (point, index) {
    var subPath = index === 0 ? ['M', point.x, point.y] : ['L', point.x, point.y];
    path.push(subPath);
  });
  return path;
}