function readFile (filePath, done) {
    fs.stat(filePath, function (err, stat) {
      if (err) {
        delete self.files[filePath]
        done()
      } else {
        self.files[filePath] = stat
        done()
      }
    })
  }