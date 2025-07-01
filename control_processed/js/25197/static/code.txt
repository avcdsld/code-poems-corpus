function(p) {
        if (typeof p === "undefined") {
            return this.__paths;
        } else {
            if (p.audio) this.__paths.audio = p.audio;
            if (p.images) this.__paths.images = p.images;
        }
    }