function prefChangeHandler() {
        var prefs = getPreferences();

        if (prefs.closeBelow !== menuEntriesShown.closeBelow) {
            if (prefs.closeBelow) {
                workingSetListCmenu.addMenuItem(closeBelow, "", Menus.AFTER, Commands.FILE_CLOSE);
            } else {
                workingSetListCmenu.removeMenuItem(closeBelow);
            }
        }

        if (prefs.closeOthers !== menuEntriesShown.closeOthers) {
            if (prefs.closeOthers) {
                workingSetListCmenu.addMenuItem(closeOthers, "", Menus.AFTER, Commands.FILE_CLOSE);
            } else {
                workingSetListCmenu.removeMenuItem(closeOthers);
            }
        }

        if (prefs.closeAbove !== menuEntriesShown.closeAbove) {
            if (prefs.closeAbove) {
                workingSetListCmenu.addMenuItem(closeAbove, "", Menus.AFTER, Commands.FILE_CLOSE);
            } else {
                workingSetListCmenu.removeMenuItem(closeAbove);
            }
        }

        menuEntriesShown = prefs;
    }