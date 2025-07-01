function DOMUpdater(previousDOM, editor, changeList) {
        var text, startOffset = 0, startOffsetPos;

        this.isIncremental = false;

        function isDangerousEdit(text) {
            // We don't consider & dangerous since entities only affect text content, not
            // overall DOM structure.
            return (/[<>\/=\"\']/).test(text);
        }

        // If there's more than one change, be conservative and assume we have to do a full reparse.
        if (changeList && changeList.length === 1) {
            // If the inserted or removed text doesn't have any characters that could change the
            // structure of the DOM (e.g. by adding or removing a tag boundary), then we can do
            // an incremental reparse of just the parent tag containing the edit. This should just
            // be the marked range that contains the beginning of the edit range, since that position
            // isn't changed by the edit.
            var change = changeList[0];
            if (!isDangerousEdit(change.text) && !isDangerousEdit(change.removed)) {
                // If the edit is right at the beginning or end of a tag, we want to be conservative
                // and use the parent as the edit range.
                var startMark = _getMarkerAtDocumentPos(editor, change.from, true);
                if (startMark) {
                    var range = startMark.find();
                    if (range) {
                        text = editor._codeMirror.getRange(range.from, range.to);
                        this.changedTagID = startMark.tagID;
                        startOffsetPos = range.from;
                        startOffset = editor._codeMirror.indexFromPos(startOffsetPos);
                        this.isIncremental = true;
                    }
                }
            }
        }

        if (!this.changedTagID) {
            // We weren't able to incrementally update, so just rebuild and diff everything.
            text = editor.document.getText();
        }

        HTMLSimpleDOM.Builder.call(this, text, startOffset, startOffsetPos);
        this.editor = editor;
        this.cm = editor._codeMirror;
        this.previousDOM = previousDOM;
    }