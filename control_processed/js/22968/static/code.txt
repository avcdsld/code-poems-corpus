function existHunkHeader(line, lineIdx) {
      var idx = lineIdx;

      while (idx < diffLines.length - 3) {
        if (utils.startsWith(line, 'diff')) {
          return false;
        }

        if (
          utils.startsWith(diffLines[idx], oldFileNameHeader) &&
          utils.startsWith(diffLines[idx + 1], newFileNameHeader) &&
          utils.startsWith(diffLines[idx + 2], hunkHeaderPrefix)
        ) {
          return true;
        }

        idx++;
      }

      return false;
    }