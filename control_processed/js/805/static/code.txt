function softwareUpdate_getElement(spec) {
    var elem = null;

    switch(spec.type) {
      /**
       * subtype: subtype to match
       * value: value to match
       */
      case "button":
        elem = new elementslib.Lookup(this._controller.window.document,
                                      WIZARD_BUTTONS_BOX + WIZARD_BUTTON[spec.subtype]);
        break;
      case "wizard":
        elem = new elementslib.Lookup(this._controller.window.document, WIZARD);
        break;
      case "wizard_page":
        elem = new elementslib.Lookup(this._controller.window.document, WIZARD_DECK +
                                      '/id(' + spec.subtype + ')');
        break;
      case "download_progress":
        elem = new elementslib.ID(this._controller.window.document, "downloadProgress");
        break;
      default:
        throw new Error(arguments.callee.name + ": Unknown element type - " + spec.type);
    }

    return elem;
  }