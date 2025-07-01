function(
  element,
  toolName,
  options,
  interactionTypes
) {
  // If interactionTypes was passed in via options
  if (interactionTypes === undefined && Array.isArray(options)) {
    interactionTypes = options;
    options = null;
  }

  const tool = getToolForElement(element, toolName);

  if (tool) {
    _resolveInputConflicts(element, tool, options, interactionTypes);

    // Iterate over specific interaction types and set active
    // This is used as a secondary check on active tools to find the active "parts" of the tool
    tool.supportedInteractionTypes.forEach(interactionType => {
      if (
        interactionTypes === undefined ||
        interactionTypes.includes(interactionType)
      ) {
        options[`is${interactionType}Active`] = true;
      } else {
        options[`is${interactionType}Active`] = false;
      }
    });

    if (
      globalConfiguration.state.showSVGCursors &&
      tool.supportedInteractionTypes.includes('Mouse')
    ) {
      _setToolCursorIfPrimary(element, options, tool);
    }
  }

  // Resume normal behavior
  setToolModeForElement('active', null, element, toolName, options);
}