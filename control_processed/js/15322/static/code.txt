function(callback, method, path, queryParams, data, prefix,
                                localTimeoutMs) {
        return this.request(
            callback, method, path, queryParams, data, {
                localTimeoutMs: localTimeoutMs,
                prefix: prefix,
            },
        );
    }