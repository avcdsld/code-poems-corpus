function scanTextUntil(cm, startCh, startLine, condition) {
        var line = cm.getLine(startLine),
            seen = "",
            characterIndex = startCh,
            currentLine = startLine,
            range;
        while (currentLine <= cm.lastLine()) {
            if (line.length === 0) {
                characterIndex = 0;
                line = cm.getLine(++currentLine);
            } else {
                seen = seen.concat(line[characterIndex] || "");
                if (condition(seen)) {
                    range = {
                        from: {ch: startCh, line: startLine},
                        to: {ch: characterIndex, line: currentLine},
                        string: seen
                    };
                    return range;
                } else if (characterIndex >= line.length) {
                    seen = seen.concat(cm.lineSeparator());
                    if (condition(seen)) {
                        range = {
                            from: {ch: startCh, line: startLine},
                            to: {ch: characterIndex, line: currentLine},
                            string: seen
                        };
                        return range;
                    }
                    characterIndex = 0;
                    line = cm.getLine(++currentLine);
                } else {
                    ++characterIndex;
                }
            }
        }
    }