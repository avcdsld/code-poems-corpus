function tryServeWithGzip() {
      fs.stat(gzippedFile, (err, stat) => {
        if (!err && stat.isFile()) {
          hasGzipId12(gzippedFile, (gzipErr, isGzip) => {
            if (!gzipErr && isGzip) {
              file = gzippedFile;
              serve(stat);
            } else {
              statFile();
            }
          });
        } else {
          statFile();
        }
      });
    }