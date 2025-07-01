function unique(array) {
    "use strict";
    var o = {},
        r = [];
    for (var i = 0, len = array.length; i !== len; i++) {
        var d = array[i];
        if (typeof o[d] === "undefined") {
            o[d] = 1;
            r[r.length] = d;
        }
    }
    return r;
}