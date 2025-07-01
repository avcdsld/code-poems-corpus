function(url, repeat) {
        this.__image = url;
        this._repeat = repeat || "no-repeat";

        this.img = Crafty.asset(url);
        if (!this.img) {
            this.img = new Image();
            Crafty.asset(url, this.img);
            this.img.src = url;
            var self = this;

            this.img.onload = function() {
                self._setupImage(self._drawLayer);
            };
        } else {
            this._setupImage(this._drawLayer);
        }

        this.trigger("Invalidate");

        return this;
    }