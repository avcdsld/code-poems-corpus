function findCommonPrefix(extractDir, callback) {
    fs.readdir(extractDir, function (err, files) {
        ignoredFolders.forEach(function (folder) {
            var index = files.indexOf(folder);
            if (index !== -1) {
                files.splice(index, 1);
            }
        });
        if (err) {
            callback(err);
        } else if (files.length === 1) {
            var name = files[0];
            if (fs.statSync(path.join(extractDir, name)).isDirectory()) {
                callback(null, name);
            } else {
                callback(null, "");
            }
        } else {
            callback(null, "");
        }
    });
}