function rhumbBearing(start, end, options = {}) {
    let bear360;
    if (options.final) bear360 = calculateRhumbBearing(end, start);
    else bear360 = calculateRhumbBearing(start, end);

    const bear180 = (bear360 > 180) ? -(360 - bear360) : bear360;

    return bear180;
}