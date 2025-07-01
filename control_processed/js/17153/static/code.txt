function addJSIndent(file, t) {
    var addIndent = '  ';
    var filepath = file.path.replace(/\\/g, '/');
    if (
      filepath.endsWith('/global/js/wrap_start.js') ||
      filepath.endsWith('/global/js/wrap_end.js')
    ) {
      addIndent = '';
    }

    if (addIndent !== '') {
      var fileLines = fs.readFileSync(file.path).toString().split('\n');
      var newFileContents = '';
      $.each(fileLines, function (i, fileLine) {
        newFileContents +=
          (fileLine ? addIndent : '') +
          fileLine +
          (i === fileLines.length ? '' : '\n');
      });

      file.contents = new Buffer(newFileContents);
    }
  }