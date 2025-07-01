function _resolveGenericInputConflicts(
  interactionType,
  tool,
  element,
  options
) {
  const interactionTypeFlag = `is${interactionType}Active`;
  const activeToolWithActiveInteractionType = store.state.tools.find(
    t =>
      t.element === element &&
      t.mode === 'active' &&
      t.options[interactionTypeFlag] === true
  );

  if (activeToolWithActiveInteractionType) {
    logger.log(
      "Setting tool %s's %s to false",
      activeToolWithActiveInteractionType.name,
      interactionTypeFlag
    );
    activeToolWithActiveInteractionType.options[interactionTypeFlag] = false;
  }
}