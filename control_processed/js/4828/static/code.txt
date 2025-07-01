function exists(path, callback) {
        stat(path, function (err) {
            if (err) {
                if (err === FileSystemError.NOT_FOUND) {
                    callback(null, false);
                } else {
                    callback(err);
                }
                return;
            }

            callback(null, true);
        });
    }