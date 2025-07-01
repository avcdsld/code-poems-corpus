function ContextMenu(id) {
        Menu.apply(this, arguments);

        var $newMenu = $("<li class='dropdown context-menu' id='" + StringUtils.jQueryIdEscape(id) + "'></li>"),
            $popUp = $("<ul class='dropdown-menu'></ul>"),
            $toggle = $("<a href='#' class='dropdown-toggle' data-toggle='dropdown'></a>").hide();

        // assemble the menu fragments
        $newMenu.append($toggle).append($popUp);

        // insert into DOM
        $("#context-menu-bar > ul").append($newMenu);

        var self = this;
        PopUpManager.addPopUp($popUp,
            function () {
                self.close();
            },
            false);

        // Listen to ContextMenu's beforeContextMenuOpen event to first close other popups
        PopUpManager.listenToContextMenu(this);
    }