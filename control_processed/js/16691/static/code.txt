function postTransformComponent (
  el,
  options
) {
  // $flow-disable-line (we know isReservedTag is there)
  if (!options.isReservedTag(el.tag) && el.tag !== 'cell-slot') {
    addAttr(el, RECYCLE_LIST_MARKER, 'true');
  }
}