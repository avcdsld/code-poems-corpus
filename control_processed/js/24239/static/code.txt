function andObservables(observables) {
    return observables.pipe(Object(rxjs_operators__WEBPACK_IMPORTED_MODULE_3__["mergeAll"])(), Object(rxjs_operators__WEBPACK_IMPORTED_MODULE_3__["every"])(function (result) { return result === true; }));
}