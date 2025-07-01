function _getPrefsContext() {
        var projectRoot = ProjectManager.getProjectRoot();  // note: null during unit tests!
        return { location : { scope: "user", layer: "project", layerID: projectRoot && projectRoot.fullPath } };
    }