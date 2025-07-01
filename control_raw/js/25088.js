function(x, y) {
        var i = 0,
            p = this.points,
            l = p.length;
        for (; i < l; i += 2) {
            p[i] += x;
            p[i + 1] += y;
        }
    }