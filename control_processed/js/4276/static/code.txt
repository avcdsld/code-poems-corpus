function goNextPrevDoc(inc, listOrder) {
        var result;
        if (listOrder) {
            result = MainViewManager.traverseToNextViewInListOrder(inc);
        } else {
            result = MainViewManager.traverseToNextViewByMRU(inc);
        }

        if (result) {
            var file = result.file,
                paneId = result.paneId;

            MainViewManager.beginTraversal();
            CommandManager.execute(Commands.FILE_OPEN, {fullPath: file.fullPath,
                                                        paneId: paneId });

            // Listen for ending of Ctrl+Tab sequence
            if (!_addedNavKeyHandler) {
                _addedNavKeyHandler = true;
                $(window.document.body).keyup(detectDocumentNavEnd);
            }
        }
    }