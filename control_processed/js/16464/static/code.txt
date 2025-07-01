function _computeMarkerId(highlight, transform, { maxZoom }) {
    const mMax = maxZoom / 4;
    const lMax = maxZoom / 2;
    const size = _getMarkerSize(transform, mMax, lMax);
    const highlighted = highlight ? HIGHLIGHTED : "";
    const markerKey = _markerKeyBuilder(size, highlighted);

    return MARKERS[markerKey];
}