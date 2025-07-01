function setSelected(record) {
    var self = this;
    var shapes = self.getShapes();
    Util.each(shapes, function (shape) {
      var origin = shape.get('origin');
      if (origin && origin[FIELD_ORIGIN] === record) {
        self.setShapeSelected(shape);
      }
    });
    return this;
  }