function addRuleToDocument(doc, selector, useTabChar, indentUnit) {
        var newRule = "\n" + selector + " {\n",
            blankLineOffset;
        if (useTabChar) {
            newRule += "\t";
            blankLineOffset = 1;
        } else {
            var i;
            for (i = 0; i < indentUnit; i++) {
                newRule += " ";
            }
            blankLineOffset = indentUnit;
        }
        newRule += "\n}\n";

        var docLines = doc.getText().split("\n"),
            lastDocLine = docLines.length - 1,
            lastDocChar = docLines[docLines.length - 1].length;
        doc.replaceRange(newRule, {line: lastDocLine, ch: lastDocChar});
        return {
            range: {
                from: {line: lastDocLine + 1, ch: 0},
                to: {line: lastDocLine + 3, ch: 1}
            },
            pos: {line: lastDocLine + 2, ch: blankLineOffset}
        };
    }