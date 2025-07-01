function () {

        var backupFile;

        var source = this.source;
        var dirname = this.dirname;
        var basename = this.basename;

        // version < 0.2.1
        if (fs.existsSync(source + '.backup')) {
            backupFile = source + '.backup';
        } else {
            backupFile = path.join(dirname, '.font-spider', basename);
        }

        if (fs.existsSync(backupFile)) {
            utils.cp(backupFile, source);
        } else {
            utils.cp(source, backupFile);
        }
    }