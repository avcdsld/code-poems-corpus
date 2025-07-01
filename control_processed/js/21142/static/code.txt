function (el, width, height) {
        // FIXME Text element not consider textAlign and textVerticalAlign.

        // TODO, inner text, shadow
        var rect = el.getBoundingRect();

        // FIXME aspect ratio
        if (width == null) {
            width = rect.width;
        }
        if (height == null) {
            height = rect.height;
        }
        width *= this.dpr;
        height *= this.dpr;

        this._fitElement(el, width, height);

        // var aspect = el.scale[1] / el.scale[0];
        // Adjust aspect ratio to make the text more clearly
        // FIXME If height > width, width is useless ?
        // width = height * aspect;
        // el.position[0] *= aspect;
        // el.scale[0] = el.scale[1];

        var x = this._x;
        var y = this._y;

        var canvasWidth = this.width * this.dpr;
        var canvasHeight = this.height * this.dpr;
        var gap = this.gap;

        if (x + width + gap > canvasWidth) {
            // Change a new row
            x = this._x = 0;
            y += this._rowHeight + gap;
            this._y = y;
            // Reset row height
            this._rowHeight = 0;
        }

        this._x += width + gap;

        this._rowHeight = Math.max(this._rowHeight, height);

        if (y + height + gap > canvasHeight) {
            // There is no space anymore
            return null;
        }

        // Shift the el
        el.position[0] += this.offsetX * this.dpr + x;
        el.position[1] += this.offsetY * this.dpr + y;

        this._zr.add(el);

        var coordsOffset = [
            this.offsetX / this.width,
            this.offsetY / this.height
        ];
        var coords = [
            [x / canvasWidth + coordsOffset[0], y / canvasHeight + coordsOffset[1]],
            [(x + width) / canvasWidth + coordsOffset[0], (y + height) / canvasHeight + coordsOffset[1]]
        ];

        return coords;
    }