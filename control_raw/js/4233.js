function _createEditorForDocument(doc, makeMasterEditor, container, range, editorOptions) {
        var editor = new Editor(doc, makeMasterEditor, container, range, editorOptions);

        editor.on("focus", function () {
            _notifyActiveEditorChanged(editor);
        });

        editor.on("beforeDestroy", function () {
            if (editor.$el.is(":visible")) {
                _saveEditorViewState(editor);
            }
        });

        return editor;
    }