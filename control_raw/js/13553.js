function (a, b) {
        vec3.cross(this.array, a.array, b.array);
        this._dirty = true;
        return this;
    }