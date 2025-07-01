function (id, buttonState) {
    var evtName;
    var previousButtonState = this.buttonStates[id];

    // Not changed.
    if (buttonState.pressed === previousButtonState.pressed) { return false; }

    evtName = buttonState.pressed ? EVENTS.BUTTONDOWN : EVENTS.BUTTONUP;
    this.el.emit(evtName, this.buttonEventDetails[id], false);
    previousButtonState.pressed = buttonState.pressed;
    return true;
  }