function (p) {
        var _min = this.min.array;
        var _max = this.max.array;

        var _p = p.array;

        return _min[0] <= _p[0] && _min[1] <= _p[1] && _min[2] <= _p[2]
            && _max[0] >= _p[0] && _max[1] >= _p[1] && _max[2] >= _p[2];
    }