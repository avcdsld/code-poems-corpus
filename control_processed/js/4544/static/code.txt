function notifyFileDeleted(file) {
        // Notify all editors to close as well
        exports.trigger("pathDeleted", file.fullPath);

        var doc = getOpenDocumentForPath(file.fullPath);

        if (doc) {
            doc.trigger("deleted");
        }

        // At this point, all those other views SHOULD have released the Doc
        if (doc && doc._refCount > 0) {
            console.warn("Deleted " + file.fullPath + " Document still has " + doc._refCount + " references. Did someone addRef() without listening for 'deleted'?");
        }
    }