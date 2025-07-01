function makeBoundingBox(bb) {
  if (bb == null) {
    return {
      x1: Infinity,
      y1: Infinity,
      x2: -Infinity,
      y2: -Infinity,
      w: 0,
      h: 0
    };
  } else if (bb.x1 != null && bb.y1 != null) {
    if (bb.x2 != null && bb.y2 != null && bb.x2 >= bb.x1 && bb.y2 >= bb.y1) {
      return {
        x1: bb.x1,
        y1: bb.y1,
        x2: bb.x2,
        y2: bb.y2,
        w: bb.x2 - bb.x1,
        h: bb.y2 - bb.y1
      };
    } else if (bb.w != null && bb.h != null && bb.w >= 0 && bb.h >= 0) {
      return {
        x1: bb.x1,
        y1: bb.y1,
        x2: bb.x1 + bb.w,
        y2: bb.y1 + bb.h,
        w: bb.w,
        h: bb.h
      };
    }
  }
}