function getOverflowStyles(e) {
    // When the <html> element has an overflow style of 'visible', it assumes
    // the overflow style of the body, and the body is really overflow:visible.
    var overflowElem = e;
    if (htmlOverflowStyle == 'visible') {
      // Note: bodyElem will be null/undefined in SVG documents.
      if (e == htmlElem && bodyElem) {
        overflowElem = bodyElem;
      } else if (e == bodyElem) {
        return {x: 'visible', y: 'visible'};
      }
    }
    var overflow = {
      x: bot.dom.getEffectiveStyle(overflowElem, 'overflow-x'),
      y: bot.dom.getEffectiveStyle(overflowElem, 'overflow-y')
    };
    // The <html> element cannot have a genuine 'visible' overflow style,
    // because the viewport can't expand; 'visible' is really 'auto'.
    if (e == htmlElem) {
      overflow.x = overflow.x == 'visible' ? 'auto' : overflow.x;
      overflow.y = overflow.y == 'visible' ? 'auto' : overflow.y;
    }
    return overflow;
  }