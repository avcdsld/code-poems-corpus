function (file, ext) {
        var fileHandler = _.find(this.handlers, function (handler) {
            return _.includes(handler.extensions, ext);
        });

        return fileHandler.loadFile([_.pick(file, 'name', 'path')]).then(function (loadedData) {
            // normalize the returned data
            var importData = {};
            importData[fileHandler.type] = loadedData;
            return importData;
        });
    }