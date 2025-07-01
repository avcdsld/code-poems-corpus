function _updateUIStates() {
        var spriteIndex,
            ICON_CLASSES = ["splitview-icon-none", "splitview-icon-vertical", "splitview-icon-horizontal"],
            layoutScheme = MainViewManager.getLayoutScheme();

        if (layoutScheme.columns > 1) {
            spriteIndex = 1;
        } else if (layoutScheme.rows > 1) {
            spriteIndex = 2;
        } else {
            spriteIndex = 0;
        }

        // SplitView Icon
        $splitViewMenu.removeClass(ICON_CLASSES.join(" "))
                      .addClass(ICON_CLASSES[spriteIndex]);

        // SplitView Menu
        _cmdSplitNone.setChecked(spriteIndex === 0);
        _cmdSplitVertical.setChecked(spriteIndex === 1);
        _cmdSplitHorizontal.setChecked(spriteIndex === 2);

        // Options icon
        _updateWorkingSetState();
    }