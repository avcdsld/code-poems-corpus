function (bbox) {
        var min = this.min;
        var max = this.max;
        vec3.min(min.array, min.array, bbox.min.array);
        vec3.max(max.array, max.array, bbox.max.array);
        min._dirty = true;
        max._dirty = true;
        return this;
    }