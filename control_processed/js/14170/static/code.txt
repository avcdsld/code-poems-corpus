function(enabledElement) {
  if (store.modules) {
    _cleanModulesOnElement(enabledElement);
  }

  const foundElementIndex = store.state.enabledElements.findIndex(
    element => element === enabledElement
  );

  if (foundElementIndex > -1) {
    store.state.enabledElements.splice(foundElementIndex, 1);
  } else {
    logger.warn('unable to remove element');
  }
}