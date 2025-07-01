function parseCookieValue(cookieStr, name) {
    var e_1, _a;
    name = encodeURIComponent(name);
    try {
        for (var _b = Object(tslib__WEBPACK_IMPORTED_MODULE_1__["__values"])(cookieStr.split(';')), _c = _b.next(); !_c.done; _c = _b.next()) {
            var cookie = _c.value;
            var eqIndex = cookie.indexOf('=');
            var _d = Object(tslib__WEBPACK_IMPORTED_MODULE_1__["__read"])(eqIndex == -1 ? [cookie, ''] : [cookie.slice(0, eqIndex), cookie.slice(eqIndex + 1)], 2), cookieName = _d[0], cookieValue = _d[1];
            if (cookieName.trim() === name) {
                return decodeURIComponent(cookieValue);
            }
        }
    }
    catch (e_1_1) { e_1 = { error: e_1_1 }; }
    finally {
        try {
            if (_c && !_c.done && (_a = _b.return)) _a.call(_b);
        }
        finally { if (e_1) throw e_1.error; }
    }
    return null;
}