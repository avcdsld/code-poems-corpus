function(evt, x, y) {

        if (!this.can('vertexAdd')) return;

        // Store the index at which the new vertex has just been placed.
        // We'll be update the very same vertex position in `pointermove()`.
        var vertexIdx = this.addVertex({ x: x, y: y }, { ui: true });
        this.eventData(evt, {
            action: 'vertex-move',
            vertexIdx: vertexIdx
        });
    }