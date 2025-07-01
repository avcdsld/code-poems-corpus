function (id, value) {
            if (!_.isEqual(this.data[id], value)) {
                this._dirty = true;
                if (value === undefined) {
                    delete this.data[id];
                } else {
                    this.data[id] = _.cloneDeep(value);
                }
                return true;
            }
            return false;
        }