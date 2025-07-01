function _pointMouseMove(e) {
        var self = e.target,
            bezierEditor = self.bezierEditor,
            curveBoundingBox = bezierEditor._getCurveBoundingBox(),
            left = curveBoundingBox.left,
            top  = curveBoundingBox.top,
            x = e.pageX - left,
            y = e.pageY - top - HEIGHT_ABOVE;

        updateTimeProgression(bezierEditor.curve, x, y);

        if (e.pageX === 0 && e.pageY === 0) {
            return;
        }

        handlePointMove(e, x, y);
    }