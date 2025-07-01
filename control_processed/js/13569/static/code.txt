function (bbox) {
        var min = this.min;
        var max = this.max;
        vec3Copy(min.array, bbox.min.array);
        vec3Copy(max.array, bbox.max.array);
        min._dirty = true;
        max._dirty = true;
        return this;
    }