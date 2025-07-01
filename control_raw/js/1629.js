function (file) {
        var self = this;

        return this.extractZip(file.path).then(function (zipDirectory) {
            var ops = [],
                importData = {},
                baseDir;

            self.isValidZip(zipDirectory);
            baseDir = self.getBaseDirectory(zipDirectory);

            _.each(self.handlers, function (handler) {
                if (importData.hasOwnProperty(handler.type)) {
                    // This limitation is here to reduce the complexity of the importer for now
                    return Promise.reject(new common.errors.UnsupportedMediaTypeError({
                        message: common.i18n.t('errors.data.importer.index.zipContainsMultipleDataFormats')
                    }));
                }

                var files = self.getFilesFromZip(handler, zipDirectory);

                if (files.length > 0) {
                    ops.push(function () {
                        return handler.loadFile(files, baseDir).then(function (data) {
                            importData[handler.type] = data;
                        });
                    });
                }
            });

            if (ops.length === 0) {
                return Promise.reject(new common.errors.UnsupportedMediaTypeError({
                    message: common.i18n.t('errors.data.importer.index.noContentToImport')
                }));
            }

            return sequence(ops).then(function () {
                return importData;
            });
        });
    }