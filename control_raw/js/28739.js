function(config, extras, callback) {

    // load all files in the source folder
    vfs.src(config.fonts.files)

      // vinyl-fs dest automatically determines whether a file
      // should be updated or not, based on the mtime timestamp.
      // so we don't need to do that manually.
      .pipe(vfs.dest(path.join(extras.destination, config.fonts.destination)))
      .on('finish', function() {
        callback(null, config, extras);
      });
  }