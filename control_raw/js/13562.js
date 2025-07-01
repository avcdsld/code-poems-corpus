function (min, max) {

    /**
     * Minimum coords of bounding box
     * @type {clay.Vector3}
     */
    this.min = min || new Vector3(Infinity, Infinity, Infinity);

    /**
     * Maximum coords of bounding box
     * @type {clay.Vector3}
     */
    this.max = max || new Vector3(-Infinity, -Infinity, -Infinity);

    this.vertices = null;
}