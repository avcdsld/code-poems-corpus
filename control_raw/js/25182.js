function(rect) {
        rect = rect || this._viewportRect();
        var gl = this.context;

        // Set viewport and clear it
        gl.viewport(0, 0, gl.viewportWidth, gl.viewportHeight);
        gl.clear(gl.COLOR_BUFFER_BIT | gl.DEPTH_BUFFER_BIT);

        //Set the viewport uniform variables used by each registered program
        var programs = this.programs;
        if (this._dirtyViewport) {
            var view = this._viewportRect();
            for (var comp in programs) {
                programs[comp].setViewportUniforms(view, this.options);
            }
            this._dirtyViewport = false;
        }

        // Search for any entities in the given area (viewport unless otherwise specified)
        var q = Crafty.map.search(rect),
            i = 0,
            l = q.length,
            current;
        //From all potential candidates, build a list of visible entities, then sort by zorder
        var visible_gl = this.visible_gl;
        visible_gl.length = 0;
        for (i = 0; i < l; i++) {
            current = q[i];
            if (
                current._visible &&
                current.program &&
                current._drawLayer === this
            ) {
                visible_gl.push(current);
            }
        }
        visible_gl.sort(this._sort);
        l = visible_gl.length;

        // Now iterate through the z-sorted entities to be rendered
        // Each entity writes it's data into a typed array
        // The entities are rendered in batches, where the entire array is copied to a buffer in one operation
        // A batch is rendered whenever the next element needs to use a different type of program
        // Therefore, you get better performance by grouping programs by z-order if possible.
        // (Each sprite sheet will use a different program, but multiple sprites on the same sheet can be rendered in one batch)
        var shaderProgram = null;
        for (i = 0; i < l; i++) {
            current = visible_gl[i];
            if (shaderProgram !== current.program) {
                if (shaderProgram !== null) {
                    shaderProgram.renderBatch();
                }

                shaderProgram = current.program;
                shaderProgram.index_pointer = 0;
                shaderProgram.switchTo();
            }
            current.draw();
            current._changed = false;
        }

        if (shaderProgram !== null) {
            shaderProgram.renderBatch();
        }
    }