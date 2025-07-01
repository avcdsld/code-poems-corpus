function (evt) {
    var shortcutPressed = evt.keyCode === 83 && evt.ctrlKey && evt.altKey;
    if (!this.data || !shortcutPressed) { return; }
    var projection = evt.shiftKey ? 'equirectangular' : 'perspective';
    this.capture(projection);
  }