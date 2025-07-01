function beforeLoc(loc, line, column) {
            if (line < loc.start.line) {
                return true;
            }
            return line === loc.start.line && column < loc.start.column;
        }