function (idx, arr) {
        var indices = this.indices;
        indices[idx * 3] = arr[0];
        indices[idx * 3 + 1] = arr[1];
        indices[idx * 3 + 2] = arr[2];
    }