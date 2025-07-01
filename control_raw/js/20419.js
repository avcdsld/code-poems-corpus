function (coords) {
        return _.isObject(coords) && !((this.position === coords.position) && (this.iteration === coords.iteration));
    }