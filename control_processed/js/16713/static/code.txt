function updateComponentData (
  componentId,
  newData,
  callback
) {
  if (!document || !document.taskCenter) {
    warn("Can't find available \"document\" or \"taskCenter\".");
    return
  }
  if (typeof document.taskCenter.updateData === 'function') {
    return document.taskCenter.updateData(componentId, newData, callback)
  }
  warn(("Failed to update component data (" + componentId + ")."));
}