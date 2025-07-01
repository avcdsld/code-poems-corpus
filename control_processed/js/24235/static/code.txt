function exportNgVar(name, value) {
    if (typeof COMPILED === 'undefined' || !COMPILED) {
        // Note: we can't export `ng` when using closure enhanced optimization as:
        // - closure declares globals itself for minified names, which sometimes clobber our `ng` global
        // - we can't declare a closure extern as the namespace `ng` is already used within Google
        //   for typings for angularJS (via `goog.provide('ng....')`).
        var ng = _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵglobal"]['ng'] = _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵglobal"]['ng'] || {};
        ng[name] = value;
    }
}