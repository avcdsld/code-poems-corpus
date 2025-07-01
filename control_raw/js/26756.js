function onComment(block, text, start, stop, startLoc, endLoc) {
      var match;
      commentsByEndLine[endLoc.line] = {
        text: text,
        block: block
      };
      match = text.match(/@module (\w+)/);
      if (match) {
        moduleName = match[1];
        modules.push({
          name: moduleName,
          comment: '/*' + text + '*/\n'
        });
      }
      // Both @module and @namespace may be defined in the same comment block.
      match = text.match(/@(namespace|module) \w+/g);
      if (match) {
        if (text.match(/@method/)) {
          // Don't allow temporary namespace renamings
          // in method block.
          return;
        }
        var namespace = match[match.length - 1].match(/@(namespace|module) (\w+)/)[2];
        namespaceBoundary(namespace, endLoc.line);
      }
    }