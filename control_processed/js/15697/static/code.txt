function(p, opt) {

        var polylines = this.toPolylines(opt);
        if (!polylines) return false; // shortcut (this path has no polylines)

        var numPolylines = polylines.length;

        // how many component polylines does `p` lie within?
        var numIntersections = 0;
        for (var i = 0; i < numPolylines; i++) {
            var polyline = polylines[i];
            if (polyline.containsPoint(p)) {
                // `p` lies within this polyline
                numIntersections++;
            }
        }

        // returns `true` for odd numbers of intersections (even-odd algorithm)
        return ((numIntersections % 2) === 1);
    }