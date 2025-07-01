function parsePoints(points) {
    var coord = this._coord;
    var rst = [];
    Util.each(points, function (point) {
      rst.push(coord.convertPoint(point));
    });
    return rst;
  }