function() {
        var ctx = this._drawContext;
        ctx.font = this._fontString();
        this.w = ctx.measureText(this._text).width;

        var size = this._textFont.size || this.defaultSize;
        this.h = 1.1 * this._getFontHeight(size);

        /* Offset the MBR for text alignment*/
        if (this._textAlign === "left" || this._textAlign === "start") {
            this.offsetBoundary(0, 0, 0, 0);
        } else if (this._textAlign === "center") {
            this.offsetBoundary(this.w / 2, 0, -this.w / 2, 0);
        } else if (this._textAlign === "end" || this._textAlign === "right") {
            this.offsetBoundary(this.w, 0, -this.w, 0);
        }
    }