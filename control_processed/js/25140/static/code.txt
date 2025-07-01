function(obj, prop, getCallback, setCallback) {
        Object.defineProperty(obj, prop, {
            get: getCallback,
            set: setCallback,
            configurable: false,
            enumerable: true
        });
    }