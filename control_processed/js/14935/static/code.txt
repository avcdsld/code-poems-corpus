function dig(obj, selector) {
        var result = obj;
        var splitter = selector.split('.');

        for (var i = 0; i < splitter.length; i++) {
          if (typeof result === 'undefined' || result === null) {
            return undefined;
          }

          result = result[splitter[i]];
        }

        return result;
      }