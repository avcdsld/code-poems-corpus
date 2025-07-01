function findNext(editor, searchBackwards, preferNoScroll, pos) {
        var cm = editor._codeMirror;
        cm.operation(function () {
            var state = getSearchState(cm);
            clearCurrentMatchHighlight(cm, state);

            var nextMatch = _getNextMatch(editor, searchBackwards, pos);
            if (nextMatch) {
                // Update match index indicators - only possible if we have resultSet saved (missing if FIND_MAX_FILE_SIZE threshold hit)
                if (state.resultSet.length) {
                    _updateFindBarWithMatchInfo(state,
                                                {from: nextMatch.start, to: nextMatch.end}, searchBackwards);
                    // Update current-tickmark indicator - only if highlighting enabled (disabled if FIND_HIGHLIGHT_MAX threshold hit)
                    if (state.marked.length) {
                        ScrollTrackMarkers.markCurrent(state.matchIndex);  // _updateFindBarWithMatchInfo() has updated this index
                    }
                }

                _selectAndScrollTo(editor, [nextMatch], true, preferNoScroll);

                // Only mark text with "current match" highlight if search bar still open
                if (findBar && !findBar.isClosed()) {
                    // If highlighting disabled, apply both match AND current-match styles for correct appearance
                    var curentMatchClassName = state.marked.length ? "searching-current-match" : "CodeMirror-searching searching-current-match";
                    state.markedCurrent = cm.markText(nextMatch.start, nextMatch.end,
                         { className: curentMatchClassName, startStyle: "searching-first", endStyle: "searching-last" });
                }
            } else {
                cm.setCursor(editor.getCursorPos());  // collapses selection, keeping cursor in place to avoid scrolling
                // (nothing more to do: previous highlights already cleared above)
            }
        });
    }