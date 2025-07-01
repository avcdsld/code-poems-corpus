function findTransferables(source, parent = null, property = null, list = []) {
    if (!source) {
        return list;
    }

    if (Array.isArray(source)) {
        // Check each array element
        source.forEach((x, i) => findTransferables(x, source, i, list));
    }
    else if (typeof source === 'object') {
        // Is the object a transferable array buffer?
        if (source instanceof ArrayBuffer) {
            list.push({ object: source, parent, property });
        }
        // Or looks like a typed array (has an array buffer property)?
        else if (source.buffer instanceof ArrayBuffer) {
            list.push({ object: source.buffer, parent, property });
        }
        // Otherwise check each property
        else {
            for (let prop in source) {
                findTransferables(source[prop], source, prop, list);
            }
        }
    }
    return list;
}