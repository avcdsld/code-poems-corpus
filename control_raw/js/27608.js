function poly2path(polygon) {
  var pos = polygon.pos;
  var points = polygon.calcPoints;
  var result = 'M' + pos.x + ' ' + pos.y;
  result += 'M' + (pos.x + points[0].x) + ' ' + (pos.y + points[0].y);
  for (var i = 1; i < points.length; i++) {
    var point = points[i];
    result += 'L' + (pos.x + point.x) + ' ' + (pos.y + point.y);
  }
  result += 'Z';
  return result;
}