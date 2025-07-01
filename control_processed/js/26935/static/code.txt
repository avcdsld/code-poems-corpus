function _readFC5(data, next) {
    var dataAddress = data.readUInt16BE(2);
    var state = data.readUInt16BE(4);

    if (next)
        next(null, { "address": dataAddress, "state": (state === 0xff00) });
}