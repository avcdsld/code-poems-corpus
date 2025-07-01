function (filePath) {
        const tmpDir = path.join(os.tmpdir(), uuid.v4());
        this.fileToDelete = tmpDir;

        return Promise.promisify(extract)(filePath, {dir: tmpDir}).then(function () {
            return tmpDir;
        });
    }