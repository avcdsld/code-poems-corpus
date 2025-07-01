function checkModifierKeys(oEvent, bCtrlKey, bAltKey, bShiftKey) {
		return oEvent.shiftKey == bShiftKey && oEvent.altKey == bAltKey && getCtrlKey(oEvent) == bCtrlKey;
	}