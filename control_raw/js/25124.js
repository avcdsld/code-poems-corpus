function() {
        if (this.length === 1 && !this.__frozen) {
            this.trigger("Freeze", this);
            this._freezeCallbacks();
            this.__frozen = true;
        } else {
            for (var i = 0; i < this.length; i++) {
                var e = entities[this[i]];
                if (e && !e.__frozen) {
                    e.trigger("Freeze", e);
                    e._freezeCallbacks();
                    // Set a frozen flag.  (This is distinct from the __callbackFrozen flag)
                    e.__frozen = true;
                }
            }
        }
        return this;
    }