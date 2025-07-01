function getFragmentAround(session, start) {
        var minIndent = null,
            minLine   = null,
            endLine,
            cm        = session.editor._codeMirror,
            tabSize   = cm.getOption("tabSize"),
            document  = session.editor.document,
            p,
            min,
            indent,
            line;

        // expand range backwards
        for (p = start.line - 1, min = Math.max(0, p - 100); p >= min; --p) {
            line = session.getLine(p);
            var fn = line.search(/\bfunction\b/);

            if (fn >= 0) {
                indent = CodeMirror.countColumn(line, null, tabSize);
                if (minIndent === null || minIndent > indent) {
                    if (session.getToken({line: p, ch: fn + 1}).type === "keyword") {
                        minIndent = indent;
                        minLine = p;
                    }
                }
            }
        }

        if (minIndent === null) {
            minIndent = 0;
        }

        if (minLine === null) {
            minLine = min;
        }

        var max = Math.min(cm.lastLine(), start.line + 100),
            endCh = 0;

        for (endLine = start.line + 1; endLine < max; ++endLine) {
            line = cm.getLine(endLine);

            if (line.length > 0) {
                indent = CodeMirror.countColumn(line, null, tabSize);
                if (indent <= minIndent) {
                    endCh = line.length;
                    break;
                }
            }
        }

        var from = {line: minLine, ch: 0},
            to   = {line: endLine, ch: endCh};

        return {type: MessageIds.TERN_FILE_INFO_TYPE_PART,
            name: document.file.fullPath,
            offsetLines: from.line,
            text: document.getRange(from, to)};
    }