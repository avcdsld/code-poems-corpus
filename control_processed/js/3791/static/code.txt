function blockComment(editor) {
        editor = editor || EditorManager.getFocusedEditor();
        if (!editor) {
            return;
        }

        var edits = [],
            lineCommentSels = [];
        _.each(editor.getSelections(), function (sel) {
            var mode = editor.getModeForRange(sel.start, sel.end),
                edit = {edit: [], selection: [sel]}; // default edit in case we don't have a mode for this selection
            if (mode) {
                var language = editor.document.getLanguage().getLanguageForMode(mode.name || mode);

                if (language.hasBlockCommentSyntax()) {
                    // getLineCommentPrefixes always return an array, and will be empty if no line comment syntax is defined
                    edit = _getBlockCommentPrefixSuffixEdit(editor, language.getBlockCommentPrefix(), language.getBlockCommentSuffix(),
                                                            language.getLineCommentPrefixes(), sel);
                    if (!edit) {
                        // This is only null if the block comment code found that the selection is within a line-commented line.
                        // Add this to the list of line-comment selections we need to handle. Since edit is null, we'll skip
                        // pushing anything onto the edit list for this selection.
                        lineCommentSels.push(sel);
                    }
                }
            }
            if (edit) {
                edits.push(edit);
            }
        });

        // Handle any line-comment edits. It's okay if these are out-of-order with the other edits, since
        // they shouldn't overlap, and `doMultipleEdits()` will take care of sorting the edits so the
        // selections can be tracked appropriately.
        edits.push.apply(edits, _getLineCommentEdits(editor, lineCommentSels, "block"));

        editor.setSelections(editor.document.doMultipleEdits(edits));
    }