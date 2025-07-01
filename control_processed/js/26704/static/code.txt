function getY(event) {
  let originalEvent = event.originalEvent;
  let touches = originalEvent? originalEvent.changedTouches : event.changedTouches;
  let touch = touches && touches[0];

  if (touch) {
    return touch.screenY;
  } else {
    return event.clientY;
  }
}