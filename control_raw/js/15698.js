function(ratio, opt) {

        var segments = this.segments;
        var numSegments = segments.length;
        if (numSegments === 0) return null; // if segments is an empty array

        if (ratio < 0) ratio = 0;
        if (ratio > 1) ratio = 1;

        opt = opt || {};
        var precision = (opt.precision === undefined) ? this.PRECISION : opt.precision;
        var segmentSubdivisions = (opt.segmentSubdivisions === undefined) ? this.getSegmentSubdivisions({ precision: precision }) : opt.segmentSubdivisions;
        var localOpt = { precision: precision, segmentSubdivisions: segmentSubdivisions };

        var pathLength = this.length(localOpt);
        var length = pathLength * ratio;

        return this.divideAtLength(length, localOpt);
    }