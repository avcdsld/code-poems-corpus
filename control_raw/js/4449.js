function updateFromDownload(installationResult) {
        if (installationResult.keepFile === undefined) {
            installationResult.keepFile = false;
        }

        var installationStatus = installationResult.installationStatus;
        if (installationStatus === Package.InstallationStatuses.ALREADY_INSTALLED ||
                installationStatus === Package.InstallationStatuses.NEEDS_UPDATE ||
                installationStatus === Package.InstallationStatuses.SAME_VERSION ||
                installationStatus === Package.InstallationStatuses.OLDER_VERSION) {
            var id = installationResult.name;
            delete _idsToRemove[id];
            _idsToUpdate[id] = installationResult;
            exports.trigger("statusChange", id);
        }
    }