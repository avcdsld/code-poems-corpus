function perspective (fovy, aspect, near, far) {
    var f = 1.0 / Math.tan(fovy / 2)
    var nf = 1 / (near - far)

    return [
      f / aspect, 0.0, 0.0, 0.0,
      0.0, f, 0.0, 0.0,
      0.0, 0.0, (far + near) * nf, -1.0,
      0.0, 0.0, (2 * far * near) * nf, 0.0
    ]
  }