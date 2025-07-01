function Cropper(element) {
    var options = arguments.length > 1 && arguments[1] !== undefined ? arguments[1] : {};
    classCallCheck(this, Cropper);

    if (!element || !REGEXP_TAG_NAME.test(element.tagName)) {
      throw new Error('The first argument is required and must be an <img> or <canvas> element.');
    }

    this.element = element;
    this.options = assign({}, DEFAULTS, isPlainObject(options) && options);
    this.cropped = false;
    this.disabled = false;
    this.pointers = {};
    this.ready = false;
    this.reloading = false;
    this.replaced = false;
    this.sized = false;
    this.sizing = false;
    this.init();
  }