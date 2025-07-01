function initializeCommands() {
        CommandManager.register(Strings.CMD_TOGGLE_PURE_CODE, CMD_TOGGLE_PURE_CODE, _togglePureCode);
        CommandManager.register(Strings.CMD_TOGGLE_PANELS, CMD_TOGGLE_PANELS, _togglePanels);

        Menus.getMenu(Menus.AppMenuBar.VIEW_MENU).addMenuItem(CMD_TOGGLE_PANELS, "", Menus.AFTER, Commands.VIEW_HIDE_SIDEBAR);
        Menus.getMenu(Menus.AppMenuBar.VIEW_MENU).addMenuItem(CMD_TOGGLE_PURE_CODE, "", Menus.AFTER, CMD_TOGGLE_PANELS);

        KeyBindingManager.addBinding(CMD_TOGGLE_PURE_CODE, [ {key: togglePureCodeKey}, {key: togglePureCodeKeyMac, platform: "mac"} ]);

        //default toggle panel shortcut was ctrl+shift+` as it is present in one vertical line in the keyboard. However, we later learnt
        //from IQE team than non-English keyboards does not have the ` char. So added one more shortcut ctrl+shift+1 which will be preferred
        KeyBindingManager.addBinding(CMD_TOGGLE_PANELS, [ {key: togglePanelsKey}, {key: togglePanelsKeyMac, platform: "mac"} ]);
        KeyBindingManager.addBinding(CMD_TOGGLE_PANELS, [ {key: togglePanelsKey_EN}, {key: togglePanelsKeyMac_EN, platform: "mac"} ]);
    }