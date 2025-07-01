function init(paths) {
        var params = new UrlParams();

        if (_init) {
            // Only init once. Return a resolved promise.
            return new $.Deferred().resolve().promise();
        }

        if (!paths) {
            params.parse();

            if (params.get("reloadWithoutUserExts") === "true") {
                paths = ["default"];
            } else {
                paths = [
                    getDefaultExtensionPath(),
                    "dev",
                    getUserExtensionPath()
                ];
            }
        }

        // Load extensions before restoring the project

        // Get a Directory for the user extension directory and create it if it doesn't exist.
        // Note that this is an async call and there are no success or failure functions passed
        // in. If the directory *doesn't* exist, it will be created. Extension loading may happen
        // before the directory is finished being created, but that is okay, since the extension
        // loading will work correctly without this directory.
        // If the directory *does* exist, nothing else needs to be done. It will be scanned normally
        // during extension loading.
        var extensionPath = getUserExtensionPath();
        FileSystem.getDirectoryForPath(extensionPath).create();

        // Create the extensions/disabled directory, too.
        var disabledExtensionPath = extensionPath.replace(/\/user$/, "/disabled");
        FileSystem.getDirectoryForPath(disabledExtensionPath).create();

        var promise = Async.doSequentially(paths, function (item) {
            var extensionPath = item;

            // If the item has "/" in it, assume it is a full path. Otherwise, load
            // from our source path + "/extensions/".
            if (item.indexOf("/") === -1) {
                extensionPath = FileUtils.getNativeBracketsDirectoryPath() + "/extensions/" + item;
            }

            return loadAllExtensionsInNativeDirectory(extensionPath);
        }, false);

        promise.always(function () {
            _init = true;
        });

        return promise;
    }