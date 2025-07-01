function font(size) {
    var cssText = selectors + '{ font-size: ' + size + 'px; }',
        el = document.createElement('style');

    el.type = 'text/css';
    if (el.styleSheet) {
      el.styleSheet.cssText = cssText;//IE only
    } else {
      el.appendChild(document.createTextNode(cssText));
    }
    head.appendChild(el);
  }