function handleKeydown(keyCodes, e, callback) {
    const keyCode = e.charCode || e.keyCode;
    if (keyCodes.indexOf(keyCode) !== -1) {
        callback();
    }
}