function noop(name) {
    return function() {
        var args = Array.prototype.slice.call(arguments);
        if (singleton) {
            return singleton[name].apply(singleton, args);
        } else {
            if (publicUtils.isStreamArg(name, args)) {
                return new PassThrough({ objectMode: true });
            }
        }
    };
}