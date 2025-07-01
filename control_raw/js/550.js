function RoamController(zr) {

    /**
     * @type {Function}
     */
    this.pointerChecker;

    /**
     * @type {module:zrender}
     */
    this._zr = zr;

    /**
     * @type {Object}
     */
    this._opt = {};

    // Avoid two roamController bind the same handler
    var bind = zrUtil.bind;
    var mousedownHandler = bind(mousedown, this);
    var mousemoveHandler = bind(mousemove, this);
    var mouseupHandler = bind(mouseup, this);
    var mousewheelHandler = bind(mousewheel, this);
    var pinchHandler = bind(pinch, this);

    Eventful.call(this);

    /**
     * @param {Function} pointerChecker
     *                   input: x, y
     *                   output: boolean
     */
    this.setPointerChecker = function (pointerChecker) {
        this.pointerChecker = pointerChecker;
    };

    /**
     * Notice: only enable needed types. For example, if 'zoom'
     * is not needed, 'zoom' should not be enabled, otherwise
     * default mousewheel behaviour (scroll page) will be disabled.
     *
     * @param  {boolean|string} [controlType=true] Specify the control type,
     *                          which can be null/undefined or true/false
     *                          or 'pan/move' or 'zoom'/'scale'
     * @param {Object} [opt]
     * @param {Object} [opt.zoomOnMouseWheel=true] The value can be: true / false / 'shift' / 'ctrl' / 'alt'.
     * @param {Object} [opt.moveOnMouseMove=true] The value can be: true / false / 'shift' / 'ctrl' / 'alt'.
     * @param {Object} [opt.moveOnMouseWheel=false] The value can be: true / false / 'shift' / 'ctrl' / 'alt'.
     * @param {Object} [opt.preventDefaultMouseMove=true] When pan.
     */
    this.enable = function (controlType, opt) {

        // Disable previous first
        this.disable();

        this._opt = zrUtil.defaults(zrUtil.clone(opt) || {}, {
            zoomOnMouseWheel: true,
            moveOnMouseMove: true,
            // By default, wheel do not trigger move.
            moveOnMouseWheel: false,
            preventDefaultMouseMove: true
        });

        if (controlType == null) {
            controlType = true;
        }

        if (controlType === true || (controlType === 'move' || controlType === 'pan')) {
            zr.on('mousedown', mousedownHandler);
            zr.on('mousemove', mousemoveHandler);
            zr.on('mouseup', mouseupHandler);
        }
        if (controlType === true || (controlType === 'scale' || controlType === 'zoom')) {
            zr.on('mousewheel', mousewheelHandler);
            zr.on('pinch', pinchHandler);
        }
    };

    this.disable = function () {
        zr.off('mousedown', mousedownHandler);
        zr.off('mousemove', mousemoveHandler);
        zr.off('mouseup', mouseupHandler);
        zr.off('mousewheel', mousewheelHandler);
        zr.off('pinch', pinchHandler);
    };

    this.dispose = this.disable;

    this.isDragging = function () {
        return this._dragging;
    };

    this.isPinching = function () {
        return this._pinching;
    };
}