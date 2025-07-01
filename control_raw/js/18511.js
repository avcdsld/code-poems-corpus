function getCurrentRegistry(cbk) {
    npm.load(function(err, conf) {
        if (err) return exit(err);
        cbk(npm.config.get('registry'));
    });
}