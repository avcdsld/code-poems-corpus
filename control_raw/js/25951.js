function onDoubleClick(event) {
    const array = getMousePosition(
      inspector.container,
      event.clientX,
      event.clientY
    );
    onDoubleClickPosition.fromArray(array);
    const intersectedEl = mouseCursor.components.cursor.intersectedEl;
    if (!intersectedEl) {
      return;
    }
    Events.emit('objectfocus', intersectedEl.object3D);
  }