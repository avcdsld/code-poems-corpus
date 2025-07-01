function(v) {
        //var theta = -1 * (v % 360); //angle always between 0 and 359
        var difference = this._rotation - v;
        // skip if there's no rotation!
        if (difference === 0) return;
        else this._rotation = v;

        this._calculateMBR();

        this.trigger("Rotate", difference);
    }