function lineComment(editor) {
        editor = editor || EditorManager.getFocusedEditor();
        if (!editor) {
            return;
        }

        editor.setSelections(editor.document.doMultipleEdits(_getLineCommentEdits(editor, editor.getSelections(), "line")));
    }