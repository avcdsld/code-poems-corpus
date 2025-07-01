function(searchTerm) {
    var suggestions = [ ];
    var popup = this.getElement({type: "searchBar_autoCompletePopup"});
    var treeElem = this.getElement({type: "searchBar_suggestions"});

    // Enter search term and wait for the popup
    this.type(searchTerm);

    this._controller.waitForEval("subject.popup.state == 'open'", TIMEOUT, 100,
                                 {popup: popup.getNode()});
    this._controller.waitForElement(treeElem, TIMEOUT);

    // Get all suggestions
    var tree = treeElem.getNode();
    this._controller.waitForEval("subject.tree.view != null", TIMEOUT, 100,
                                 {tree: tree});
    for (var i = 0; i < tree.view.rowCount; i ++) {
      suggestions.push(tree.view.getCellText(i, tree.columns.getColumnAt(0)));
    }

    // Close auto-complete popup
    this._controller.keypress(popup, "VK_ESCAPE", {});
    this._controller.waitForEval("subject.popup.state == 'closed'", TIMEOUT, 100,
                                 {popup: popup.getNode()});

    return suggestions;
  }