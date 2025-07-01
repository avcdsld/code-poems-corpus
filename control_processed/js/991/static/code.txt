function DOMWalker_processNode(activeNode, idSet) {
    var doc = this._controller.window.document;
    var nodeToProcess = this._getNode(idSet);

    // Opens a new window/dialog through a menulist and runs DOMWalker.walk()
    // for it.
    // If the wanted window/dialog is already selected, just run this function
    // recursively for it's descendants.
    if (activeNode.localName == "menulist") {
      if (nodeToProcess.label != idSet.title) {
        var dropDown = new elementslib.Elem(nodeToProcess);
        this._controller.waitForElement(dropDown);

        this._controller.select(dropDown, null, idSet.title);

        this._controller.waitFor(function() {
          return nodeToProcess.label == idSet.title;
        }, "The menu item did not load in time: " + idSet.title);

        // If the target is a new modal/non-modal window, this.walk() has to be
        // started by the method opening that window. If not, we do it here.
        if (idSet.target == DOMWalker.WINDOW_CURRENT)
          this.walk(idSet.subContent, null, idSet.waitFunction);
      } else if (nodeToProcess.selected && idSet.subContent &&
                 idSet.subContent.length > 0) {
        this._prepareTargetWindows(idSet.subContent);
      }
    }

    // Opens a new prefpane using a provided windowHandler object
    // and runs DOMWalker.walk() for it.
    // If the wanted prefpane is already selected, just run this function
    // recursively for it's descendants.
    else if (activeNode.localName == "prefpane") {
      var windowHandler = idSet.windowHandler;

      if (windowHandler.paneId != idSet.id) {
        windowHandler.paneId = idSet.id;

        // Wait for the pane's content to load and to be fully displayed
        this._controller.waitFor(function() {
          return (nodeToProcess.loaded &&
                  (!mozmill.isMac ||
                   nodeToProcess.style.opacity == 1 ||
                   nodeToProcess.style.opacity == null));
        }, "The pane did not load in time: " + idSet.id);

        // If the target is a new modal/non-modal window, this.walk() has to be
        // started by the method opening that window. If not, we do it here.
        if (idSet.target == DOMWalker.WINDOW_CURRENT)
          this.walk(idSet.subContent, null, idSet.waitFunction);
      } else if (windowHandler.paneId == idSet.id && idSet.subContent &&
                 idSet.subContent.length > 0) {
        this._prepareTargetWindows(idSet.subContent);
      }
    }

    // Switches to another tab and runs DOMWalker.walk() for it.
    // If the wanted tabpanel is already selected, just run this function
    // recursively for it's descendants.
    else if (activeNode.localName == "tab") {
      if (nodeToProcess.selected != true) {
        this._controller.click(new elementslib.Elem(nodeToProcess));

        // If the target is a new modal/non-modal window, this.walk() has to be
        // started by the method opening that window. If not, we do it here.
        if (idSet.target == DOMWalker.WINDOW_CURRENT)
          this.walk(idSet.subContent, null, idSet.waitFunction);
      } else if (nodeToProcess.selected && idSet.subContent
                 && idSet.subContent.length > 0) {
        this._prepareTargetWindows(idSet.subContent);
      }
    }

    // Opens a new dialog/window by clicking on an object and runs
    // DOMWalker.walk() for it.
    else {
      this._controller.click(new elementslib.Elem(nodeToProcess));

      // If the target is a new modal/non-modal window, this.walk() has to be
      // started by the method opening that window. If not, we do it here.
      if (idSet.target == DOMWalker.WINDOW_CURRENT)
        this.walk(idSet.subContent, null, idSet.waitFunction);
    }
  }