function(cell) {
    cellsize = cell || 64;
    this.map = {};

    this.boundsDirty = false;
    this.coordBoundsDirty = false;
    this.boundsHash = {
        maxX: -Infinity,
        maxY: -Infinity,
        minX: Infinity,
        minY: Infinity
    };
    this.boundsCoords = {
        maxX: -Infinity,
        maxY: -Infinity,
        minX: Infinity,
        minY: Infinity
    };
}