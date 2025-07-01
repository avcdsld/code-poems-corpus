function(time) {
            if (this.pulldown && !this.disablePulldown) {
                if (this.y >= this.options.down.height) {
                    this.pulldownLoading(undefined, time || 0);
                    return true;
                } else {
                    !this.loading && this.topPocket.classList.remove(CLASS_VISIBILITY);
                }
            }
            return this._super(time);
        }