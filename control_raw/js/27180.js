function(files, options, parsers) {
    return Q.Promise(function(resolve, reject) {
      var filePromises = [],
        sections = [];

      // Process every file
      Object.keys(files).forEach(function(filePath) {
        var contents = files[filePath],
          syntax = path.extname(filePath).substring(1),
          parser = parsers  ? parsers[syntax] : 'undefined';
        filePromises.push(processFile(contents, filePath, syntax, options, parser));
      });
      // All files are processed
      Q.all(filePromises).then(function(results) {
        // Combine sections from every file to a single array
        results.map(function(result) {
          var fileSections = result.valueOf();
          if (fileSections && fileSections.length > 0) {
            sections = sections.concat(fileSections);
          }
        });

        // Sort sections by reference number and call main promise
        try {
          sections.sort(bySectionReference);
          resolve(sections);
        } catch (err) {
          reject(err);
        }
      }).catch(reject);
    });
  }