function findInAllWorkingSets(fullPath) {
        var index,
            result = [];

        _.forEach(_panes, function (pane) {
            index = pane.findInViewList(fullPath);
            if (index >= 0) {
                result.push({paneId: pane.id, index: index});
            }
        });

        return result;
    }