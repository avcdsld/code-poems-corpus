function getPathsMatchingFilter(compiledFilter, filePaths) {
        if (!compiledFilter) {
            return filePaths;
        }

        var re = new RegExp(compiledFilter);
        return filePaths.filter(function (f) {
            return f.match(re);
        });
    }