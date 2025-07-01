function(index, arg) {

        var segments = this.segments;
        var numSegments = segments.length;
        if (numSegments === 0) throw new Error('Path has no segments.');

        if (index < 0) index = numSegments + index; // convert negative indices to positive
        if (index >= numSegments || index < 0) throw new Error('Index out of range.');

        var currentSegment;

        var replacedSegment = segments[index];
        var previousSegment = replacedSegment.previousSegment;
        var nextSegment = replacedSegment.nextSegment;

        var updateSubpathStart = replacedSegment.isSubpathStart; // boolean: is an update of subpath starts necessary?

        if (!Array.isArray(arg)) {
            if (!arg || !arg.isSegment) throw new Error('Segment required.');

            currentSegment = this.prepareSegment(arg, previousSegment, nextSegment);
            segments.splice(index, 1, currentSegment); // directly replace

            if (updateSubpathStart && currentSegment.isSubpathStart) updateSubpathStart = false; // already updated by `prepareSegment`

        } else {
            // flatten one level deep
            // so we can chain arbitrary Path.createSegment results
            arg = arg.reduce(function(acc, val) {
                return acc.concat(val);
            }, []);

            if (!arg[0].isSegment) throw new Error('Segments required.');

            segments.splice(index, 1);

            var n = arg.length;
            for (var i = 0; i < n; i++) {

                var currentArg = arg[i];
                currentSegment = this.prepareSegment(currentArg, previousSegment, nextSegment);
                segments.splice((index + i), 0, currentSegment); // incrementing index to insert subsequent segments after inserted segments
                previousSegment = currentSegment;

                if (updateSubpathStart && currentSegment.isSubpathStart) updateSubpathStart = false; // already updated by `prepareSegment`
            }
        }

        // if replaced segment used to start a subpath and no new subpath start was added, update all subsequent segments until another subpath start segment is reached
        if (updateSubpathStart && nextSegment) this.updateSubpathStartSegment(nextSegment);
    }