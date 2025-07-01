function _changeEncodingAndReloadDoc(document) {
        var promise = document.reload();
        promise.done(function (text, readTimestamp) {
            encodingSelect.$button.text(document.file._encoding);
            // Store the preferred encoding in the state
            var projectRoot = ProjectManager.getProjectRoot(),
                context = {
                    location : {
                        scope: "user",
                        layer: "project",
                        layerID: projectRoot.fullPath
                    }
                };
            var encoding = PreferencesManager.getViewState("encoding", context);
            encoding[document.file.fullPath] = document.file._encoding;
            PreferencesManager.setViewState("encoding", encoding, context);
        });
        promise.fail(function (error) {
            console.log("Error reloading contents of " + document.file.fullPath, error);
        });
    }