function intersection (frame, otherFrame) {
  var x = Math.max(frame.x, otherFrame.x);
  var width = Math.min(frame.x + frame.width, otherFrame.x + otherFrame.width);
  var y = Math.max(frame.y, otherFrame.y);
  var height = Math.min(frame.y + frame.height, otherFrame.y + otherFrame.height);
  if (width >= x && height >= y) {
    return make(x, y, width - x, height - y);
  }
  return null;
}