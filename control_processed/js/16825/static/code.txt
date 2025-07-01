function getDocking(point, referenceElement, moveAxis) {

  var referenceMid,
      inverseAxis;

  if (point.original) {
    return point.original;
  } else {
    referenceMid = getMid(referenceElement);
    inverseAxis = flipAxis(moveAxis);

    return axisSet(point, inverseAxis, referenceMid[inverseAxis]);
  }
}