function createLines(sourcePoint, targetPoint, route) {
        // make a flattened array of all points
        var points = [].concat(sourcePoint, route, targetPoint);
        return points.reduce(function(resultLines, point, idx) {
            // if there is a next point, make a line with it
            var nextPoint = points[idx + 1];
            if (nextPoint != null) {
                resultLines[idx] = g.line(point, nextPoint);
            }
            return resultLines;
        }, []);
    }