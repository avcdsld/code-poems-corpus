function() {

        var sinks = [];
        joint.util.forIn(this._nodes, function(exists, node) {
            if (!this._out[node] || joint.util.isEmpty(this._out[node])) {
                sinks.push(this.getCell(node));
            }
        }.bind(this));
        return sinks;
    }