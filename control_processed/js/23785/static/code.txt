function print() {
        var parts = String(out).split('\n');
        /* istanbul ignore next */
        if (parts.length > 1) {
          out = parts.pop();
          var logging = String(parts.join('\n')).replace(/\r\r/g, '\r');
          slf.log(logging);
        }
        /* istanbul ignore next */
        if (closed === false) {
          setTimeout(function () {
            print();
          }, 50);
        }
      }