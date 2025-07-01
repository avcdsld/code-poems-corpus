function() {
        var self = this;
        var clone = new Model();
        
        Object.keys(self).forEach(function(key) {
            clone[key] = self[key];
        });
        
        Array.prototype.slice.call(arguments).forEach(function(tuple) {
            clone[tuple[0]] = tuple[1];
        });
        
        return clone;
    }