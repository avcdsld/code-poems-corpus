function _removeFileFromMRU(paneId, file) {
        var index,
            compare = function (record) {
                return (record.file === file && record.paneId === paneId);
            };

        // find and remove all instances
        do {
            index = _.findIndex(_mruList, compare);
            if (index !== -1) {
                _mruList.splice(index, 1);
            }
        } while (index !== -1);
    }