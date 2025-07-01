function (url, controls) {
        var self = this;
        if (!url) {
            throw new ArgumentError(
                Logger.logMessage(Logger.LEVEL_SEVERE, "KmlFile", "constructor", "invalidDocumentPassed")
            );
        }

        // Default values.
        this._controls = controls || null;
        this._fileCache = new KmlFileCache();
        this._styleResolver = new StyleResolver(this._fileCache);
        this._listener = new RefreshListener();
        this._headers = null;

        return this.requestRemote(url).then(function (options) {
            var loadedDocument = options.text;
            self._headers = options.headers;

            if (!self.hasExtension("kmz", url)) {
                return loadedDocument;
            } else {
                var kmzFile = new KmzFile(loadedDocument, self._fileCache);
                return kmzFile.load();
            }
        }).then(function (rootDocument) {
            self._document = new XmlDocument(rootDocument).dom();
            KmlObject.call(self, {objectNode: self._document.documentElement, controls: controls});

            self._fileCache.add(url, self, true);

            return self;
        });
    }