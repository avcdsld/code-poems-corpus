function (plane, out) {
        var pn = plane.normal.array;
        var d = plane.distance;
        var ro = this.origin.array;
        var rd = this.direction.array;

        var divider = vec3.dot(pn, rd);
        // ray is parallel to the plane
        if (divider === 0) {
            return null;
        }
        if (!out) {
            out = new Vector3();
        }
        var t = (vec3.dot(pn, ro) - d) / divider;
        vec3.scaleAndAdd(out.array, ro, rd, -t);
        out._dirty = true;
        return out;
    }