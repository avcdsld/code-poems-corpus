function _saveFileList(fileList) {
        // Do in serial because doSave shows error UI for each file, and we don't want to stack
        // multiple dialogs on top of each other
        var userCanceled = false,
            filesAfterSave = [];

        return Async.doSequentially(
            fileList,
            function (file) {
                // Abort remaining saves if user canceled any Save As dialog
                if (userCanceled) {
                    return (new $.Deferred()).reject().promise();
                }

                var doc = DocumentManager.getOpenDocumentForPath(file.fullPath);
                if (doc) {
                    var savePromise = handleFileSave({doc: doc});
                    savePromise
                        .done(function (newFile) {
                            filesAfterSave.push(newFile);
                        })
                        .fail(function (error) {
                            if (error === USER_CANCELED) {
                                userCanceled = true;
                            }
                        });
                    return savePromise;
                } else {
                    // workingset entry that was never actually opened - ignore
                    filesAfterSave.push(file);
                    return (new $.Deferred()).resolve().promise();
                }
            },
            false  // if any save fails, continue trying to save other files anyway; then reject at end
        ).then(function () {
            return filesAfterSave;
        });
    }