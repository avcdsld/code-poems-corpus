function _addWelcomeProjectPath(path, currentProjects) {
        var pathNoSlash = FileUtils.stripTrailingSlash(path);  // "welcomeProjects" pref has standardized on no trailing "/"

        var newProjects;

        if (currentProjects) {
            newProjects = _.clone(currentProjects);
        } else {
            newProjects = [];
        }

        if (newProjects.indexOf(pathNoSlash) === -1) {
            newProjects.push(pathNoSlash);
        }
        return newProjects;
    }