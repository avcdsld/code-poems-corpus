function (idx, out) {
        if (idx < this.triangleCount && idx >= 0) {
            if (!out) {
                out = [];
            }
            var indices = this.indices;
            out[0] = indices[idx * 3];
            out[1] = indices[idx * 3 + 1];
            out[2] = indices[idx * 3 + 2];
            return out;
        }
    }