function isTrailingComment(line, lineNumber, comment) {
            return comment &&
                (comment.loc.start.line === lineNumber && lineNumber <= comment.loc.end.line) &&
                (comment.loc.end.line > lineNumber || comment.loc.end.column === line.length);
        }