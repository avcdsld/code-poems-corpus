function(x, y, opt) {

        // accept input in form `{ x, y }, opt` or `x, y, opt`
        var isPointProvided = (typeof x !== 'number');
        var localX = isPointProvided ? x.x : x;
        var localY = isPointProvided ? x.y : y;
        var localOpt = isPointProvided ? y : opt;

        var vertex = { x: localX, y: localY };
        var idx = this.getVertexIndex(localX, localY);
        this.model.insertVertex(idx, vertex, localOpt);
        return idx;
    }