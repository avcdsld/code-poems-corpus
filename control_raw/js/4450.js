function removeUpdate(id) {
        var installationResult = _idsToUpdate[id];
        if (!installationResult) {
            return;
        }
        if (installationResult.localPath && !installationResult.keepFile) {
            FileSystem.getFileForPath(installationResult.localPath).unlink();
        }
        delete _idsToUpdate[id];
        exports.trigger("statusChange", id);
    }