function drawMono(
    ctx, points, start, segLen, allLen,
    dir, smoothMin, smoothMax, smooth, smoothMonotone, connectNulls
) {
    var prevIdx = 0;
    var idx = start;
    for (var k = 0; k < segLen; k++) {
        var p = points[idx];
        if (idx >= allLen || idx < 0) {
            break;
        }
        if (isPointNull(p)) {
            if (connectNulls) {
                idx += dir;
                continue;
            }
            break;
        }

        if (idx === start) {
            ctx[dir > 0 ? 'moveTo' : 'lineTo'](p[0], p[1]);
        }
        else {
            if (smooth > 0) {
                var prevP = points[prevIdx];
                var dim = smoothMonotone === 'y' ? 1 : 0;

                // Length of control point to p, either in x or y, but not both
                var ctrlLen = (p[dim] - prevP[dim]) * smooth;

                v2Copy(cp0, prevP);
                cp0[dim] = prevP[dim] + ctrlLen;

                v2Copy(cp1, p);
                cp1[dim] = p[dim] - ctrlLen;

                ctx.bezierCurveTo(
                    cp0[0], cp0[1],
                    cp1[0], cp1[1],
                    p[0], p[1]
                );
            }
            else {
                ctx.lineTo(p[0], p[1]);
            }
        }

        prevIdx = idx;
        idx += dir;
    }

    return k;
}