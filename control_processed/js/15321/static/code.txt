function(callback, method, path, queryParams, data,
                                      prefix, localTimeoutMs) {
        return this.authedRequest(
            callback, method, path, queryParams, data, {
                localTimeoutMs: localTimeoutMs,
                prefix: prefix,
            },
        );
    }