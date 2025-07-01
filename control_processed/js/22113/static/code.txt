function(cb, next, method) {
        return function(value) {
            if (typeof cb !== 'function')                            /*  [Promises/A+ 2.2.1, 2.2.7.3, 2.2.7.4]  */
                next[method].call(next, value);                      /*  [Promises/A+ 2.2.7.3, 2.2.7.4]  */
            else {
                var result;
                try {
                    if (value instanceof Promise) {
                        result = value.then(cb);
                    }
                    else result = cb(value);
                }                          /*  [Promises/A+ 2.2.2.1, 2.2.3.1, 2.2.5, 3.2]  */
                catch (e) {
                    next.reject(e);                                  /*  [Promises/A+ 2.2.7.2]  */
                    return;
                }
                resolve(next, result);                               /*  [Promises/A+ 2.2.7.1]  */
            }
        };
    }