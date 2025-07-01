function statefulSelectors(
  states: Array<InteractionState>,
  template: Function,
  stateMap?: Array<InteractionState>,
): string {
  if (!template) throw new PolishedError(67)
  if (states.length === 0) return generateSelectors(template, null)
  let selectors = []
  for (let i = 0; i < states.length; i += 1) {
    if (stateMap && stateMap.indexOf(states[i]) < 0) {
      throw new PolishedError(68)
    }
    selectors.push(generateSelectors(template, states[i]))
  }
  selectors = selectors.join(',')
  return selectors
}