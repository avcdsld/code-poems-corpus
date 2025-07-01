function (projection) {
    var params = this.setCapture(projection);
    this.renderCapture(params.camera, params.size, params.projection);
    return this.canvas;
  }