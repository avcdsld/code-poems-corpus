function getFilenameWithoutExtension(filename) {
        var index = filename.lastIndexOf(".");
        return index === -1 ? filename : filename.slice(0, index);
    }