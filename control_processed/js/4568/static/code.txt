function filterPath(compiledFilter, fullPath) {
        if (!compiledFilter) {
            return true;
        }

        var re = new RegExp(compiledFilter);
        return !fullPath.match(re);
    }