function unlink(path, callback) {
        appshell.fs.unlink(path, function (err) {
            callback(_mapError(err));
        });
    }