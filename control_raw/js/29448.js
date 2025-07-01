function venn(areas, parameters) {
        parameters = parameters || {};
        parameters.maxIterations = parameters.maxIterations || 500;
        var initialLayout = parameters.initialLayout || bestInitialLayout;
        var loss = parameters.lossFunction || lossFunction;

        // add in missing pairwise areas as having 0 size
        areas = addMissingAreas(areas);

        // initial layout is done greedily
        var circles = initialLayout(areas, parameters);

        // transform x/y coordinates to a vector to optimize
        var initial = [],
            setids = [],
            setid;
        for (setid in circles) {
            if (circles.hasOwnProperty(setid)) {
                initial.push(circles[setid].x);
                initial.push(circles[setid].y);
                setids.push(setid);
            }
        }

        // optimize initial layout from our loss function
        var solution = nelderMead(function (values) {
            var current = {};
            for (var i = 0; i < setids.length; ++i) {
                var setid = setids[i];
                current[setid] = { x: values[2 * i],
                    y: values[2 * i + 1],
                    radius: circles[setid].radius
                    // size : circles[setid].size
                };
            }
            return loss(current, areas);
        }, initial, parameters);

        // transform solution vector back to x/y points
        var positions = solution.x;
        for (var i = 0; i < setids.length; ++i) {
            setid = setids[i];
            circles[setid].x = positions[2 * i];
            circles[setid].y = positions[2 * i + 1];
        }

        return circles;
    }