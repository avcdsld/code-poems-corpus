function getHeight(el, defaultValue) {
    var height = this.getStyle(el, 'height', defaultValue);
    if (height === 'auto') {
      height = el.offsetHeight;
    }
    return parseFloat(height);
  }