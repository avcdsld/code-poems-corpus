function _monkeypatch(filePath, monkeyPatched, processor, complete) {
  async.waterfall(
    [
      function read(next) {
        fs.readFile(filePath, 'utf8', next);
      },

      // TODO - need to parse gyp file - this is a bit hacker
      function monkeypatch(content, next) {
        if (monkeyPatched(content)) return complete();

        _log('monkey patch %s', filePath);
        processor(content, next);
      },

      function write(content, next) {
        fs.writeFile(filePath, content, 'utf8', function(err) {
          return next(err);
        });
      },
    ],
    complete,
  );
}