function _sortByPlatform(a, b) {
        var a1 = (a.platform) ? 1 : 0,
            b1 = (b.platform) ? 1 : 0;
        return b1 - a1;
    }