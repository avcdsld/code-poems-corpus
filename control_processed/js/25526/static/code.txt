function bnToBuffer(trimOrSize) {
    var res = new Buffer(this.toByteArray());
    if (trimOrSize === true && res[0] === 0) {
        res = res.slice(1);
    } else if (_.isNumber(trimOrSize)) {
        if (res.length > trimOrSize) {
            for (var i = 0; i < res.length - trimOrSize; i++) {
                if (res[i] !== 0) {
                    return null;
                }
            }
            return res.slice(res.length - trimOrSize);
        } else if (res.length < trimOrSize) {
            var padded = new Buffer(trimOrSize);
            padded.fill(0, 0, trimOrSize - res.length);
            res.copy(padded, trimOrSize - res.length);
            return padded;
        }
    }
    return res;
}