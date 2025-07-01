function centeringProperties(_ref3) {
    var oDim = _ref3.oDim,
        wDim = _ref3.wDim,
        tPos = _ref3.tPos,
        tDim = _ref3.tDim;
    var center = Math.round(tPos + tDim / 2);
    var leftOffset = oDim / 2 - center;
    var rightOffset = center + oDim / 2 - wDim;
    return {
      center: center,
      leftOffset: leftOffset,
      rightOffset: rightOffset
    };
  }